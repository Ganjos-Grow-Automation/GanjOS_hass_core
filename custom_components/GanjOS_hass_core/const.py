DOMAIN = "ganjos"

PLANT_STAGE_PARAMETERS = {
    "VPD-Target-Value": {
        "default": 1.2, "min": 0.5, "max": 2.0, "step": 0.1, "unit": "kPa",
        "icon": "mdi:water-percent"
    },
    "VPD-Target-Tolerance-Value": {
        "default": 0.1, "min": 0.0, "max": 0.5, "step": 0.01, "unit": "kPa",
        "icon": "mdi:water-off"
    },
    "VPD-Tolerance-Value": {
        "default": 0.2, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa",
        "icon": "mdi:water-alert"
    },
    "VPD-Notification-Difference-Value": {
        "default": 0.3, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa",
        "icon": "mdi:bell-alert-outline"
    },
    "VPD-Day-Night-Difference-Value": {
        "default": 0.5, "min": 0.0, "max": 1.5, "step": 0.1, "unit": "kPa",
        "icon": "mdi:weather-night"
    },
    "Temperature-Air-Target-Value": {
        "default": 25, "min": 15, "max": 35, "step": 0.5, "unit": "°C",
        "icon": "mdi:thermometer"
    },
    "Temperature-Air-Target-Tolerance-Value": {
        "default": 1, "min": 0, "max": 5, "step": 0.1, "unit": "°C",
        "icon": "mdi:thermometer-check"
    },
    "Temperature-Air-Tolerance-Value": {
        "default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C",
        "icon": "mdi:thermometer-lines"
    },
    "Temperature-Air-Notification-Difference-Value": {
        "default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C",
        "icon": "mdi:bell-alert"
    },
    "Temperature-Air-Day-Night-Difference-Value": {
        "default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C",
        "icon": "mdi:weather-night"
    },
    "Humidity-Target-Value": {
        "default": 60, "min": 30, "max": 90, "step": 1, "unit": "%",
        "icon": "mdi:water-percent"
    },
    "Humidity-Target-Tolerance-Value": {
        "default": 5, "min": 0, "max": 20, "step": 1, "unit": "%",
        "icon": "mdi:water-alert"
    },
    "Humidity-Tolerance-Value": {
        "default": 10, "min": 0, "max": 20, "step": 1, "unit": "%",
        "icon": "mdi:water-off"
    },
    "Humidity-Notification-Difference-Value": {
        "default": 15, "min": 0, "max": 30, "step": 1, "unit": "%",
        "icon": "mdi:bell-alert"
    },
    "Humidity-Day-Night-Difference-Value": {
        "default": 20, "min": 0, "max": 40, "step": 1, "unit": "%",
        "icon": "mdi:weather-night"
    },
    "CO2-Target-Value": {
        "default": 400, "min": 300, "max": 2000, "step": 10, "unit": "ppm",
        "icon": "mdi:molecule-co2"
    },
    "CO2-Target-Tolerance-Value": {
        "default": 50, "min": 0, "max": 200, "step": 10, "unit": "ppm",
        "icon": "mdi:molecule-co2"
    },
    "CO2-Tolerance-Value": {
        "default": 100, "min": 0, "max": 200, "step": 10, "unit": "ppm",
        "icon": "mdi:chart-bell-curve"
    },
    "CO2-Notification-Difference-Value": {
        "default": 200, "min": 0, "max": 400, "step": 10, "unit": "ppm",
        "icon": "mdi:bell-alert-outline"
    },
    "CO2-Day-Night-Difference-Value": {
        "default": 300, "min": 0, "max": 600, "step": 10, "unit": "ppm",
        "icon": "mdi:weather-night"
    },
    "Soil-Moisture-Target-Value": {
        "default": 50, "min": 10, "max": 100, "step": 1, "unit": "%",
        "icon": "mdi:cup-water"
    },
    "Soil-Moisture-Target-Tolerance-Value": {
        "default": 5, "min": 0, "max": 10, "step": 1, "unit": "%",
        "icon": "mdi:water-off"
    },
    "Soil-Moisture-Tolerance-Value": {
        "default": 10, "min": 0, "max": 20, "step": 1, "unit": "%",
        "icon": "mdi:water-alert"
    },
    "Soil-Moisture-Notification-Difference-Value": {
        "default": 15, "min": 0, "max": 30, "step": 1, "unit": "%",
        "icon": "mdi:bell-alert"
    },
    "Soil-Temperature-Target-Value": {
        "default": 20, "min": 10, "max": 30, "step": 0.5, "unit": "°C",
        "icon": "mdi:thermometer"
    },
    "Soil-Temperature-Target-Tolerance-Value": {
        "default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C",
        "icon": "mdi:thermometer-alert"
    },
    "Soil-Temperature-Tolerance-Value": {
        "default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C",
        "icon": "mdi:thermometer-lines"
    },
    "Soil-Temperature-Notification-Difference-Value": {
        "default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C",
        "icon": "mdi:bell-alert-outline"
    },
    "Light-Hours-Target-Value": {
        "default": 16, "min": 0, "max": 24, "step": 1, "unit": "hours",
        "icon": "mdi:weather-sunny"
    },
    "Light-Intensity-Target-Value": {
        "default": 1000, "min": 50, "max": 2000, "step": 50, "unit": "ppfd",
        "icon": "mdi:lightbulb-on-outline"
    }
}

