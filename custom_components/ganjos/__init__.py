import logging
from importlib.util import find_spec
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN, PLATFORMS
from .core import create_new_area, create_plant_stage, create_dry_stage

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initial setup of the GanjOS integration (before config entries)."""
    _LOGGER.info("GanjOS integration initial setup successful.")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up GanjOS from a config entry."""
    _LOGGER.info("Setting up GanjOS config entry.")
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    # Load only supported platform components
    supported_platforms = [
        platform
        for platform in PLATFORMS
        if find_spec(f"custom_components.ganjos.{platform}")
    ]
    await hass.config_entries.async_forward_entry_setups(entry, supported_platforms)

    # Register default grow area and plant stages
    await create_new_area(hass, entry, "grow", "Grow")
    await create_plant_stage(hass, entry, "veg", "Vegetative")
    await create_plant_stage(hass, entry, "bloom", "Bloom")
    #await create_dry_stage(hass, entry)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload GanjOS integration."""
    supported_platforms = [
        platform
        for platform in PLATFORMS
        if find_spec(f"custom_components.ganjos.{platform}")
    ]
    unload_ok = await hass.config_entries.async_unload_platforms(entry, supported_platforms)
    if unload_ok and DOMAIN in hass.data:
        hass.data[DOMAIN].pop(entry.entry_id, None)
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    return unload_ok
