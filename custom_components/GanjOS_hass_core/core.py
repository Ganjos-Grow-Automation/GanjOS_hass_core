import logging
from homeassistant.helpers import device_registry as dr
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN, PLANT_STAGE_PARAMETERS
from .number import create_number_entities

_LOGGER = logging.getLogger(__name__)


async def create_new_area(hass, entry: ConfigEntry, area_key: str, display_name: str):
    """Create or update a grow area device."""
    registry = dr.async_get(hass)
    device_id = area_key  # e.g. "grow"

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
        registry.async_update_device(
            device_id=existing_device.id,
            name=display_name
        )
        _LOGGER.info(f"Updated Grow Area name to: {display_name}")

    # TODO: Create other entity types here when implemented

    return device_id


async def create_plant_stage(hass, entry: ConfigEntry, stage_key: str, display_name: str):
    """Create or update a plant stage device and its number entities."""
    registry = dr.async_get(hass)
    device_id = stage_key  # e.g. "veg", "bloom"

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
        registry.async_update_device(
            device_id=existing_device.id,
            name=display_name
        )
        _LOGGER.info(f"Updated Plant Stage name to: {display_name}")

    # Create the number entities for this stage
    await create_number_entities(
        hass=hass,
        config_entry=entry,
        device_id=device_id,
        parameters=PLANT_STAGE_PARAMETERS,
        model="Plant Stage",
        name_prefix=display_name
    )

    return device_id

async def create_dry_stage(hass, entry, stage_key: str = "dry", display_name: str = "Dry"):
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
        registry.async_update_device(
            device_id=existing_device.id,
            name=display_name
        )
        _LOGGER.info(f"Updated Dry Stage name to: {display_name}")

    #await create_number_entities(
    #    hass=hass,
    #    config_entry_id=entry.entry_id,
    #    device_id=device_id,
    #    parameters=DRY_STAGE_PARAMETERS,
    #    model="Drying Stage",
    #    name_prefix=display_name
    #)

    return device_id