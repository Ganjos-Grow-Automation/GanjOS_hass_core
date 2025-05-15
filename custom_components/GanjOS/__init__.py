import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN
from .core import create_new_area, create_plant_stage

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initializes the GanjOS integration."""
    _LOGGER.info("GanjOS integration successfully loaded.")

    hass.data[DOMAIN] = {}

    # Create the central grow area device
    await create_new_area(hass, "grow", "Grow")

    # Create two standalone plant stage devices
    await create_plant_stage(hass, "veg", "Vegetative")
    await create_plant_stage(hass, "bloom", "Bloom")

    return True