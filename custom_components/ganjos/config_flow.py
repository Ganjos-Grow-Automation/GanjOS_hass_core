import logging
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class GanjosCoreConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Manage the configuration flow for GanjOS Core."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Automatically create the default configuration entry without user interaction."""
        _LOGGER.info("Initializing default config flow for GanjOS Core")
        return self.async_create_entry(
            title="GanjOS Core",
            data={"default_config": True}
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return an options flow handler if needed."""
        return GanjosCoreOptionsFlow(config_entry)


class GanjosCoreOptionsFlow(config_entries.OptionsFlow):
    """Handle options for the GanjOS Core integration."""

    def __init__(self, config_entry):
        self.config_entry = config_entry
        _LOGGER.debug("GanjOS Core options flow initialized.")

    async def async_step_init(self, user_input=None):
        """Default options step."""
        return self.async_create_entry(title="", data={})
