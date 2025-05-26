import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    """Register the add_entities callback for sensor platform."""
    hass.data.setdefault(DOMAIN, {})["sensor_platform"] = async_add_entities


async def create_sensor_entities(
    hass,
    config_entry: ConfigEntry,
    device_id: str,
    parameters: dict,
    model: str,
    name_prefix: str = ""
):
    """Create sensor entities dynamically for a given device."""
    entities = []

    for param_key, param_cfg in parameters.items():
        entity_id = f"sensor.{device_id}_{param_key}".lower().replace("-", "_")
        display_name = f"{name_prefix} {param_key.replace('-', ' ')}".strip()

        entities.append(
            GanjosSensor(
                name=display_name,
                entity_id=entity_id,
                device_id=device_id,
                param_key=param_key,
                config=param_cfg,
                model=model,
                display_device_name=name_prefix,
                config_entry=config_entry
            )
        )

    if entities:
        platform = hass.data[DOMAIN].get("sensor_platform")
        if platform:
            platform(entities)
            _LOGGER.info(f"Added {len(entities)} sensor entities for {device_id}")
        else:
            _LOGGER.warning("No entity registration function available for sensor platform.")


class GanjosSensor(SensorEntity):
    """A dynamic sensor entity used by GanjOS."""

    def __init__(
        self,
        name,
        entity_id,
        device_id,
        param_key,
        config,
        model="GanjOS Sensor",
        display_device_name=None,
        config_entry: ConfigEntry = None
    ):
        self._name = name
        self._entity_id = entity_id
        self._device_id = device_id
        self._param_key = param_key
        self._config = config
        self._model = model
        self._display_device_name = display_device_name or device_id
        self._state = config.get("default", 0)
        self._config_entry = config_entry

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{self._config_entry.entry_id}__{self._device_id}__{self._param_key}".lower()

    @property
    def native_value(self):
        return self._state

    @property
    def native_unit_of_measurement(self):
        return self._config.get("unit", None)

    @property
    def icon(self):
        return self._config.get("icon", "mdi:eye")

    @property
    def config_entry(self):
        return self._config_entry

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": self._display_device_name,
            "manufacturer": "GanjOS",
            "model": self._model,
        }