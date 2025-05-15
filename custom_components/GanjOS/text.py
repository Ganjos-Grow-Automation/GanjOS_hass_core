import logging
from homeassistant.components.text import TextEntity
from homeassistant.helpers.entity import async_generate_entity_id
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def create_text_entities(hass, context_id: str, config: dict):
    """
    Creates text entities for a given context (area or plant stage).

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        context_id (str): Identifier for the area or plant stage.
        config (dict): Dictionary of parameters and configurations.
    """
    entities = []

    for parameter, settings in config.items():
        entity_id = async_generate_entity_id(
            "text.{}",
            f"{context_id}_{parameter.lower().replace('-', '_')}",
            hass=hass
        )

        entity = GanjosTextEntity(
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

    _LOGGER.info(f"Created {len(entities)} text entities for {context_id}.")


class GanjosTextEntity(TextEntity):
    def __init__(self, context_id, parameter, config, entity_id):
        self._attr_name = f"{context_id} {parameter}"
        self._attr_unique_id = entity_id
        self._context = context_id
        self._parameter = parameter
        self._config = config
        self._state = config.get("initial", "")
        self._attr_icon = config.get("icon", "mdi:text")
        self._attr_min = config.get("min", 0)
        self._attr_max = config.get("max", 255)
        self._attr_mode = config.get("mode", "text")

    @property
    def native_value(self):
        return self._state

    async def async_set_value(self, value):
        self._state = value
        self.async_write_ha_state()

    @property
    def should_poll(self):
        return False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._context)},
            "name": self._context,
            "manufacturer": "GanjOS",
            "model": "GanjOS Text Entity"
        }
