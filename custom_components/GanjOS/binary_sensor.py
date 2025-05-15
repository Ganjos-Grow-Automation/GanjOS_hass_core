import logging
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity import async_generate_entity_id
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def create_binary_sensor_entities(hass, context_id: str, config: dict):
    """
    Creates binary sensor entities for a given context (area or plant stage).

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        context_id (str): Identifier for the area or plant stage.
        config (dict): Dictionary of parameters and configurations.
    """
    entities = []

    for parameter, settings in config.items():
        entity_id = async_generate_entity_id(
            "binary_sensor.{}",
            f"{context_id}_{parameter.lower().replace('-', '_')}",
            hass=hass
        )

        entity = GanjosBinarySensor(
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

    _LOGGER.info(f"Created {len(entities)} binary_sensor entities for {context_id}.")


class GanjosBinarySensor(BinarySensorEntity):
    def __init__(self, context_id, parameter, config, entity_id):
        self._attr_name = f"{context_id} {parameter}"
        self._attr_unique_id = entity_id
        self._context = context_id
        self._parameter = parameter
        self._config = config
        self._attr_icon = config.get("icon", "mdi:checkbox-marked-circle")
        self._attr_device_class = config.get("device_class")
        self._state = config.get("initial", False)

    @property
    def is_on(self):
        return self._state

    @property
    def should_poll(self):
        return False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._context)},
            "name": self._context,
            "manufacturer": "GanjOS",
            "model": "GanjOS Binary Sensor"
        }
