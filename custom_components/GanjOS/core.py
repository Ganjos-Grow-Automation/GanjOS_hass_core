import logging
from homeassistant.helpers.device_registry import async_get as async_get_device_registry
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def create_new_area(hass, area_id: str, area_name: str):
    """Creates a central grow area as a device."""
    registry = async_get_device_registry(hass)
    device = registry.async_get_or_create(
        config_entry_id="ganjos_static_entry",
        identifiers={(DOMAIN, area_id)},
        manufacturer="GanjOS",
        name=area_name,
        model="Grow Area",
        sw_version="0.1.0",
    )
    _LOGGER.info(f"Created Grow Area device: {area_name} with ID {area_id}")
    return device

async def create_plant_stage(hass, stage_id: str, stage_name: str):
    """Creates a plant stage as a standalone device."""
    registry = async_get_device_registry(hass)
    device = registry.async_get_or_create(
        config_entry_id="ganjos_static_entry",
        identifiers={(DOMAIN, stage_id)},
        manufacturer="GanjOS",
        name=stage_name,
        model="Plant Stage",
        sw_version="0.1.0"
    )
    _LOGGER.info(f"Created Plant Stage device: {stage_name} with ID {stage_id}")
    return device