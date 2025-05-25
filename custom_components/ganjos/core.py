import logging
from homeassistant.helpers import device_registry as dr
from homeassistant.config_entries import ConfigEntry
from .const import (
    DOMAIN,
    AREA_SETTINGS_SWITCH_PARAMETERS,
    AREA_SETTINGS_NUMBER_PARAMETERS,
    AREA_SETTINGS_TEXT_PARAMETERS,
    AREA_SETTINGS_SELECT_PARAMETERS,
    AREA_BINARY_SENSOR_PARAMETERS,
    AREA_SENSOR_PARAMETERS,
    AREA_DATE_PARAMETERS,
    PLANT_STAGE_PARAMETERS
)
from .number import create_number_entities
from .sensor import create_sensor_entities
from .switch import create_switch_entities
from .binary_sensor import create_binary_sensor_entities
from .select import create_select_entities
from .text import create_text_entities
from .datetime import create_datetime_entities

_LOGGER = logging.getLogger(__name__)


async def create_new_area(hass, entry: ConfigEntry, area_key: str, display_name: str):
    """Create or update a grow area device and its entities."""
    registry = dr.async_get(hass)
    device_id = area_key

    existing_device = registry.async_get_device({(DOMAIN, device_id)})
    if existing_device is None:
        registry.async_get_or_create(
            config_entry_id=entry.entry_id,
            identifiers={(DOMAIN, device_id)},
            manufacturer="GanjOS",
            name=display_name,
            model="Grow Area",
            sw_version="0.1.0",
        )
        _LOGGER.info(f"Created Grow Area device: {display_name}")
    else:
        registry.async_update_device(device_id=existing_device.id, name=display_name)
        _LOGGER.info(f"Updated Grow Area name to: {display_name}")

    # Entity Creation (Area Level)
    await create_switch_entities(hass, entry, device_id, AREA_SETTINGS_SWITCH_PARAMETERS, "Grow Area", display_name)
    await create_number_entities(hass, entry, device_id, AREA_SETTINGS_NUMBER_PARAMETERS, "Grow Area", display_name)
    await create_text_entities(hass, entry, device_id, AREA_SETTINGS_TEXT_PARAMETERS, "Grow Area", display_name)
    await create_select_entities(hass, entry, device_id, AREA_SETTINGS_SELECT_PARAMETERS, "Grow Area", display_name)
    await create_binary_sensor_entities(hass, entry, device_id, AREA_BINARY_SENSOR_PARAMETERS, "Grow Area", display_name)
    await create_sensor_entities(hass, entry, device_id, AREA_SENSOR_PARAMETERS, "Grow Area", display_name)
    #await create_datetime_entities(hass, entry, device_id, AREA_DATE_PARAMETERS, "Grow Area", display_name)

    return device_id


async def create_plant_stage(hass, entry: ConfigEntry, stage_key: str, display_name: str):
    """Create or update a plant stage device and its number entities."""
    registry = dr.async_get(hass)
    device_id = stage_key

    existing_device = registry.async_get_device({(DOMAIN, device_id)})
    if existing_device is None:
        registry.async_get_or_create(
            config_entry_id=entry.entry_id,
            identifiers={(DOMAIN, device_id)},
            manufacturer="GanjOS",
            name=display_name,
            model="Plant Stage",
            sw_version="0.1.0",
        )
        _LOGGER.info(f"Created Plant Stage device: {display_name}")
    else:
        registry.async_update_device(device_id=existing_device.id, name=display_name)
        _LOGGER.info(f"Updated Plant Stage name to: {display_name}")

    # Only number entities for now (can be extended)
    await create_number_entities(hass, entry, device_id, PLANT_STAGE_PARAMETERS, "Plant Stage", display_name)

    return device_id


async def create_dry_stage(hass, entry: ConfigEntry, stage_key: str = "dry", display_name: str = "Dry"):
    """Create or update a drying stage with reduced number entities."""
    registry = dr.async_get(hass)
    device_id = stage_key

    existing_device = registry.async_get_device({(DOMAIN, device_id)})
    if existing_device is None:
        registry.async_get_or_create(
            config_entry_id=entry.entry_id,
            identifiers={(DOMAIN, device_id)},
            manufacturer="GanjOS",
            name=display_name,
            model="Drying Stage",
            sw_version="0.1.0",
        )
        _LOGGER.info(f"Created Dry Stage device: {display_name}")
    else:
        registry.async_update_device(device_id=existing_device.id, name=display_name)
        _LOGGER.info(f"Updated Dry Stage name to: {display_name}")

    # Optional: await create_number_entities(...) with DRY_STAGE_PARAMETERS
    return device_id
