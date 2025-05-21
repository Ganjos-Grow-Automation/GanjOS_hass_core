import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN, PLATFORMS
from .core import create_new_area, create_plant_stage

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up GanjOS integration from a config entry."""
    _LOGGER.info("GanjOS Integration successfully loaded from config entry.")
    hass.data.setdefault(DOMAIN, {})

    # Plattformen laden (number, switch, sensor etc.)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Beispielhafte Grow Area und Pflanzphasen erzeugen
    await create_new_area(hass, entry, "grow", "Grow")
    await create_plant_stage(hass, entry, "veg", "Vegetatiove")
    await create_plant_stage(hass, entry, "bloom", "Bloom")

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle unloading of a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
        _LOGGER.info("GanjOS Integration successfully unloaded.")
    return unload_ok
