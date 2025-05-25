import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.select import SelectEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    """Register the add_entities callback for select platform."""
    hass.data.setdefault(DOMAIN, {})["select_platform"] = async_add_entities


async def create_select_entities(
    hass,
    config_entry: ConfigEntry,
    device_id: str,
    parameters: dict,
    model: str,
    name_prefix: str = ""
):
    """Create select entities dynamically for a given device."""
    entities = []

    for param_key, param_cfg in parameters.items():
        entity_id = f"select.{device_id}_{param_key}".lower().replace("-", "_")
        display_name = f"{name_prefix} {param_key.replace('-', ' ')}".strip()

        entities.append(
            GanjosSelect(
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
        platform = hass.data[DOMAIN].get("select_platform")
        if platform:
            platform(entities)
            _LOGGER.info(f"Added {len(entities)} select entities for {device_id}")
        else:
            _LOGGER.warning("No entity registration function available for select platform.")


class GanjosSelect(SelectEntity):
    """A dynamic select entity used by GanjOS."""

    def __init__(
        self,
        name,
        entity_id,
        device_id,
        param_key,
        config,
        model="GanjOS Select",
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
        self._config_entry = config_entry

        self._attr_options = config.get("options", [])
        self._attr_current_option = config.get("default", self._attr_options[0] if self._attr_options else None)

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{self._config_entry.entry_id}__{self._device_id}__{self._param_key}".lower()

    @property
    def current_option(self):
        return self._attr_current_option

    async def async_select_option(self, option: str):
        if option in self._attr_options:
            self._attr_current_option = option
            self.async_write_ha_state()

    @property
    def options(self):
        return self._attr_options

    @property
    def icon(self):
        return self._config.get("icon", "mdi:form-select")

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
            "sw_version": "0.1.0",
            "configuration_url": "https://ganjos.io",
            "entry_type": "device",
            "via_device": None
        }
