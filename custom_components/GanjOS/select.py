import logging
from homeassistant.components.select import SelectEntity
from homeassistant.helpers.entity import async_generate_entity_id
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def create_select_entities(hass, context_id: str, config: dict):
    """
    Creates select entities for a given context (area or plant stage).

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        context_id (str): Identifier for the area or plant stage.
        config (dict): Dictionary of parameters and configurations.
    """
    entities = []

    for parameter, settings in config.items():
        entity_id = async_generate_entity_id(
            "select.{}",
            f"{context_id}_{parameter.lower().replace('-', '_')}",
            hass=hass
        )

        entity = GanjosSelect(
            context_id=context_id,
            parameter=parameter,
            config=settings,
            entity_id=entity_id
        )

        entities.append(entity)

    if entities:
        async_add_entities = hass.data[DOMAIN].get("add_entities_service")
        if async_add_entities:
            async_add_entities(entities)
        else:
            _LOGGER.warning("add_entities_service not registered.")

    _LOGGER.info(f"Created {len(entities)} select entities for {context_id}.")


class GanjosSelect(SelectEntity):
    def __init__(self, context_id, parameter, config, entity_id):
        self._attr_name = f"{context_id} {parameter}"
        self._attr_unique_id = entity_id
        self._context = context_id
        self._parameter = parameter
        self._config = config
        self._attr_icon = config.get("icon", "mdi:format-list-bulleted")
        self._attr_options = config.get("options", [])
        self._attr_current_option = self._attr_options[0] if self._attr_options else None

    def select_option(self, option):
        if option in self._attr_options:
            self._attr_current_option = option
            self.schedule_update_ha_state()

    @property
    def current_option(self):
        return self._attr_current_option

    @property
    def should_poll(self):
        return False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._context)},
            "name": self._context,
            "manufacturer": "GanjOS",
            "model": "GanjOS Select"
        }