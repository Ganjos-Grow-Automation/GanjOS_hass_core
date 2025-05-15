import logging
from homeassistant.components.input_number import InputNumberEntity
from homeassistant.helpers.entity import async_generate_entity_id
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def create_input_number_entities(hass, context_id: str, config: dict):
    """
    Creates input_number entities for a given context (area or plant stage).

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        context_id (str): Identifier for the area or plant stage.
        config (dict): Dictionary of parameters and configurations.
    """
    entities = []

    for parameter, settings in config.items():
        entity_id = async_generate_entity_id(
            "input_number.{}",
            f"{context_id}_{parameter.lower().replace('-', '_')}",
            hass=hass
        )

        entity = GanjosInputNumber(
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

    _LOGGER.info(f"Created {len(entities)} input_number entities for {context_id}.")


class GanjosInputNumber(InputNumberEntity):
    def __init__(self, context_id, parameter, config, entity_id):
        self._attr_name = f"{context_id} {parameter}"
        self._attr_unique_id = entity_id
        self._context = context_id
        self._parameter = parameter
        self._config = config
        self._state = config.get("default", 0)
        self._attr_native_min_value = config.get("min", 0)
        self._attr_native_max_value = config.get("max", 100)
        self._attr_native_step = config.get("step", 1)
        self._attr_native_unit_of_measurement = config.get("unit", "")
        self._attr_icon = config.get("icon", "mdi:tune")

    @property
    def native_value(self):
        return self._state

    async def async_set_native_value(self, value):
        _LOGGER.debug(f"Setting value for {self._attr_name}: {value}")
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
            "model": "GanjOS Number"
        }
