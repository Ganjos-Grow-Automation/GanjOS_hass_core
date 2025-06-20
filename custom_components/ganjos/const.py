DOMAIN = "ganjos"

PLATFORMS = [
    "number",
    "sensor",
    "switch",
    "binary_sensor",
    "select",
    "text",
    "datetime"
]

PLANT_STAGE_PARAMETERS = {
    "VPD-Target-Value": {"default": 1.2, "min": 0.5, "max": 2.0, "step": 0.1, "unit": "kPa","icon": "mdi:water-percent"},
    "VPD-Target-Tolerance-Value": {"default": 0.1, "min": 0.0, "max": 0.5, "step": 0.01, "unit": "kPa","icon": "mdi:water-off"},
    "VPD-Tolerance-Value": {"default": 0.2, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa","icon": "mdi:water-alert"},
    "VPD-Notification-Difference-Value": {"default": 0.3, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa","icon": "mdi:bell-alert-outline"},
    "VPD-Day-Night-Difference-Value": {"default": 0.5, "min": 0.0, "max": 1.5, "step": 0.1, "unit": "kPa","icon": "mdi:weather-night"},
    "Temperature-Air-Target-Value": {"default": 25, "min": 15, "max": 35, "step": 0.5, "unit": "°C","icon": "mdi:thermometer"},
    "Temperature-Air-Target-Tolerance-Value": {"default": 1, "min": 0, "max": 5, "step": 0.1, "unit": "°C","icon": "mdi:thermometer-check"},
    "Temperature-Air-Tolerance-Value": {"default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-lines"},
    "Temperature-Air-Notification-Difference-Value": {"default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:bell-alert"},
    "Temperature-Air-Day-Night-Difference-Value": {"default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C","icon": "mdi:weather-night"},
    "Humidity-Target-Value": {"default": 60, "min": 30, "max": 90, "step": 1, "unit": "%","icon": "mdi:water-percent"},
    "Humidity-Target-Tolerance-Value": {"default": 5, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-alert"},
    "Humidity-Tolerance-Value": {"default": 10, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-off"},
    "Humidity-Notification-Difference-Value": {"default": 15, "min": 0, "max": 30, "step": 1, "unit": "%","icon": "mdi:bell-alert"},
    "Humidity-Day-Night-Difference-Value": {"default": 20, "min": 0, "max": 40, "step": 1, "unit": "%","icon": "mdi:weather-night"},
    "CO2-Target-Value": {"default": 400, "min": 300, "max": 2000, "step": 10, "unit": "ppm","icon": "mdi:molecule-co2"},
    "CO2-Target-Tolerance-Value": {"default": 50, "min": 0, "max": 200, "step": 10, "unit": "ppm","icon": "mdi:molecule-co2"},
    "CO2-Tolerance-Value": {"default": 100, "min": 0, "max": 200, "step": 10, "unit": "ppm","icon": "mdi:chart-bell-curve"},
    "CO2-Notification-Difference-Value": {"default": 200, "min": 0, "max": 400, "step": 10, "unit": "ppm","icon": "mdi:bell-alert-outline"},
    "CO2-Day-Night-Difference-Value": {"default": 300, "min": 0, "max": 600, "step": 10, "unit": "ppm","icon": "mdi:weather-night"},
    "Soil-Moisture-Target-Value": {"default": 50, "min": 10, "max": 100, "step": 1, "unit": "%","icon": "mdi:cup-water"},
    "Soil-Moisture-Target-Tolerance-Value": {"default": 5, "min": 0, "max": 10, "step": 1, "unit": "%","icon": "mdi:water-off"},
    "Soil-Moisture-Tolerance-Value": {"default": 10, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-alert"},
    "Soil-Moisture-Notification-Difference-Value": {"default": 15, "min": 0, "max": 30, "step": 1, "unit": "%","icon": "mdi:bell-alert"},
    "Soil-Temperature-Target-Value": {"default": 20, "min": 10, "max": 30, "step": 0.5, "unit": "°C","icon": "mdi:thermometer"},
    "Soil-Temperature-Target-Tolerance-Value": {"default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-alert"},
    "Soil-Temperature-Tolerance-Value": {"default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-lines"},
    "Soil-Temperature-Notification-Difference-Value": {"default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C","icon": "mdi:bell-alert-outline"},
    "Light-Hours-Target-Value": {"default": 16, "min": 0, "max": 24, "step": 1, "unit": "hours","icon": "mdi:weather-sunny"},
    "Light-Intensity-Target-Value": {"default": 1000, "min": 50, "max": 2000, "step": 50, "unit": "ppfd","icon": "mdi:lightbulb-on-outline"}
}

AREA_SETTINGS_NUMBER_PARAMETERS = {
    "Sunrise-Sunset-Duration": {"default": 30, "min": 0, "max": 120, "step": 1, "unit": "min", "icon": "mdi:weather-sunset"},
    "Leaf-Temperature-Offset": {"default": 0, "min": -10, "max": 10, "step": 0.1, "unit": "°C", "icon": "mdi:thermometer-lines"},
    "Light-Dimm-Value": {"default": 100, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:brightness-6"},
    "Light-Current-Min-Dimm": {"default": 30, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:brightness-4"},
    "Light-Current-Max-Dimm": {"default": 100, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:brightness-7"},
    "Light-Vegetative-Min-Dimm": {"default": 40, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:leaf"},
    "Light-Vegetative-Max-Dimm": {"default": 90, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:leaf"},
    "Light-Bloom-Min-Dimm": {"default": 50, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:flower"},
    "Light-Bloom-Max-Dimm": {"default": 100, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:flower"},
    "Exhaust-Dimm-Value": {"default": 80, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:fan-speed-3"},
    "Exhaust-Dehumidifier-Dimm-Value": {"default": 60, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:fan-minus"},
    "Exhaust-Min-Dimm": {"default": 30, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:fan"},
    "Exhaust-Max-Dimm": {"default": 100, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:fan"},
    "Exhaust-Interval-Power": {"default": 5, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "Ventilation-Dimm-Value": {"default": 70, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-filter"},
    "Ventilation-Min-Dimm": {"default": 40, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-filter"},
    "Ventilation-Max-Dimm": {"default": 90, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-filter"},
    "Ventilation-Interval-Power": {"default": 5, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "Heater-Dimm-Value": {"default": 60, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:radiator"},
    "Heater-Min-Dimm": {"default": 30, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:radiator"},
    "Heater-Max-Dimm": {"default": 100, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:radiator"},
    "Heater-Interval-Power": {"default": 10, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "Humidifier-Dimm-Value": {"default": 50, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-plus"},
    "Humidifier-Min-Dimm": {"default": 20, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-plus"},
    "Humidifier-Max-Dimm": {"default": 80, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-plus"},
    "Humidifier-Interval-Power": {"default": 10, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "Dehumidifier-Dimm-Value": {"default": 55, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-off"},
    "Dehumidifier-Min-Dimm": {"default": 25, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-off"},
    "Dehumidifier-Max-Dimm": {"default": 90, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:water-off"},
    "Dehumidifier-Interval-Power": {"default": 15, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "Ac-Dimm-Value": {"default": 65, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-conditioner"},
    "Ac-Min-Dimm": {"default": 30, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-conditioner"},
    "Ac-Max-Dimm": {"default": 95, "min": 0, "max": 100, "step": 1, "unit": "%", "icon": "mdi:air-conditioner"},
    "Ac-Interval-Power": {"default": 10, "min": 0, "max": 3600, "step": 5, "unit": "s", "icon": "mdi:timer-sand"},
    "VPD-Target-Setting-Value": {"default": 1.2, "min": 0.5, "max": 2.0, "step": 0.1, "unit": "kPa","icon": "mdi:water-percent"},
    "VPD-Target-Tolerance-Setting-Value": {"default": 0.1, "min": 0.0, "max": 0.5, "step": 0.01, "unit": "kPa","icon": "mdi:water-off"},
    "VPD-Tolerance-Setting-Value": {"default": 0.2, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa","icon": "mdi:water-alert"},
    "VPD-Notification-Difference-Setting-Value": {"default": 0.3, "min": 0.0, "max": 1.0, "step": 0.05, "unit": "kPa","icon": "mdi:bell-alert-outline"},
    "VPD-Day-Night-Difference-Setting-Value": {"default": 0.5, "min": 0.0, "max": 1.5, "step": 0.1, "unit": "kPa","icon": "mdi:weather-night"},
    "Temperature-Air-Target-Setting-Value": {"default": 25, "min": 15, "max": 35, "step": 0.5, "unit": "°C","icon": "mdi:thermometer"},
    "Temperature-Air-Target-Tolerance-Setting-Value": {"default": 1, "min": 0, "max": 5, "step": 0.1, "unit": "°C","icon": "mdi:thermometer-check"},
    "Temperature-Air-Tolerance-Setting-Value": {"default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-lines"},
    "Temperature-Air-Notification-Difference-Setting-Value": {"default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:bell-alert"},
    "Temperature-Air-Day-Night-Difference-Setting-Value": {"default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C","icon": "mdi:weather-night"},
    "Humidity-Target-Setting-Value": {"default": 60, "min": 30, "max": 90, "step": 1, "unit": "%","icon": "mdi:water-percent"},
    "Humidity-Target-Tolerance-Setting-Value": {"default": 5, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-alert"},
    "Humidity-Tolerance-Setting-Value": {"default": 10, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-off"},
    "Humidity-Notification-Difference-Setting-Value": {"default": 15, "min": 0, "max": 30, "step": 1, "unit": "%","icon": "mdi:bell-alert"},
    "Humidity-Day-Night-Difference-Setting-Value": {"default": 20, "min": 0, "max": 40, "step": 1, "unit": "%","icon": "mdi:weather-night"},
    "CO2-Target-Setting-Value": {"default": 400, "min": 300, "max": 2000, "step": 10, "unit": "ppm","icon": "mdi:molecule-co2"},
    "CO2-Target-Tolerance-Setting-Value": {"default": 50, "min": 0, "max": 200, "step": 10, "unit": "ppm","icon": "mdi:molecule-co2"},
    "CO2-Tolerance-Setting-Value": {"default": 100, "min": 0, "max": 200, "step": 10, "unit": "ppm","icon": "mdi:chart-bell-curve"},
    "CO2-Notification-Difference-Setting-Value": {"default": 200, "min": 0, "max": 400, "step": 10, "unit": "ppm","icon": "mdi:bell-alert-outline"},
    "CO2-Day-Night-Difference-Setting-Value": {"default": 300, "min": 0, "max": 600, "step": 10, "unit": "ppm","icon": "mdi:weather-night"},
    "Soil-Moisture-Target-Setting-Value": {"default": 50, "min": 10, "max": 100, "step": 1, "unit": "%","icon": "mdi:cup-water"},
    "Soil-Moisture-Target-Tolerance-Setting-Value": {"default": 5, "min": 0, "max": 10, "step": 1, "unit": "%","icon": "mdi:water-off"},
    "Soil-Moisture-Tolerance-Setting-Value": {"default": 10, "min": 0, "max": 20, "step": 1, "unit": "%","icon": "mdi:water-alert"},
    "Soil-Moisture-Notification-Difference-Setting-Value": {"default": 15, "min": 0, "max": 30, "step": 1, "unit": "%","icon": "mdi:bell-alert"},
    "Soil-Temperature-Target-Setting-Value": {"default": 20, "min": 10, "max": 30, "step": 0.5, "unit": "°C","icon": "mdi:thermometer"},
    "Soil-Temperature-Target-Tolerance-Setting-Value": {"default": 2, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-alert"},
    "Soil-Temperature-Tolerance-Setting-Value": {"default": 3, "min": 0, "max": 5, "step": 0.5, "unit": "°C","icon": "mdi:thermometer-lines"},
    "Soil-Temperature-Notification-Difference-Setting-Value": {"default": 5, "min": 0, "max": 10, "step": 0.5, "unit": "°C","icon": "mdi:bell-alert-outline"},
    "Light-Hours-Target-Setting-Value": {"default": 16, "min": 0, "max": 24, "step": 1, "unit": "hours","icon": "mdi:weather-sunny"},
    "Light-Intensity-Target-Setting-Value": {"default": 1000, "min": 50, "max": 2000, "step": 50, "unit": "ppfd","icon": "mdi:lightbulb-on-outline"}
}

AREA_SETTINGS_SWITCH_PARAMETERS = {
    "Area-Is-Active": {"icon": "mdi:checkbox-marked-circle-outline", "default": False},
    "Light-Available": {"icon": "mdi:lightbulb", "default": False},
    "Light-Dimmable": {"icon": "mdi:brightness-6", "default": False},
    "Exhaust-Available": {"icon": "mdi:fan", "default": False},
    "Exhaust-Dimmable": {"icon": "mdi:fan-speed-3", "default": False},
    "Exhaust-Equals-Dehumidifer": {"icon": "mdi:fan-minus", "default": False},
    "Exhaust-Equals-Ac": {"icon": "mdi:fan-plus", "default": False},
    "Ventilation-Available": {"icon": "mdi:air-filter", "default": False},
    "Ventilation-Dimmable": {"icon": "mdi:air-purifier", "default": False},
    "Heater-Available": {"icon": "mdi:radiator", "default": False},
    "Heater-Dimmable": {"icon": "mdi:radiator-disabled", "default": False},
    "Humidifier-Available": {"icon": "mdi:water", "default": False},
    "Humidifier-Dimmable": {"icon": "mdi:water-plus", "default": False},
    "Dehumidifier-Available": {"icon": "mdi:water-off", "default": False},
    "Dehumidifier-Dimmable": {"icon": "mdi:water-remove", "default": False},
    "Ac-Available": {"icon": "mdi:snowflake", "default": False},
    "Ac-Dimmable": {"icon": "mdi:air-conditioner", "default": False}
}

AREA_SETTINGS_SELECT_PARAMETERS = {
    "Light-Schedule-Mode": {"icon": "mdi:calendar-clock","options": ["18/6", "16/8","12/12","darkness"],"default": "18/6"},
    "Light-Power-Mode": {"icon": "mdi:flash","options": ["sunrise/sunset", "on/off"],"default": "on/off"},
    "Climate-Control-Mode": {"icon": "mdi:thermostat","options": ["VPD", "Temp/Hum"],"default": "VPD"},
    "Climate-Control-Prio-Value": {"icon": "mdi:swap-vertical","options": ["temperature", "humidity"],"default": "temperature"},
    "Plant-Stage": {"icon": "mdi:sprout","options": ["Vegetative", "Bloom"],"default": "Vegetative"}
}

AREA_SETTINGS_TEXT_PARAMETERS = {
    "Settings-VPD": {"icon": "mdi:chart-bell-curve","default": ""},
    "Settings-Temperature-Air": {"icon": "mdi:thermometer","default": ""},
    "Settings-Humidity": {"icon": "mdi:water-percent","default": ""},
    "Settings-Co2": {"icon": "mdi:molecule-co2", "default": ""},
    "Settings-Soil-Moisture": {"icon": "mdi:water","default": ""}
}

AREA_SENSOR_PARAMETERS = {
    "Light-General-Power-Percentage": {"icon": "mdi:lightbulb-on", "unit": "%"},
    "Light-Hours": {"icon": "mdi:clock-outline", "unit": "h"},
    "Exhaust-General-Power-Percentage": {"icon": "mdi:fan", "unit": "%"},
    "Ventilation-General-Power-Percentage": {"icon": "mdi:air-filter", "unit": "%"},
    "Heater-General-Power-Percentage": {"icon": "mdi:radiator", "unit": "%"},
    "Humidifier-General-Power-Percentage": {"icon": "mdi:water-percent", "unit": "%"},
    "Dehumidifier-General-Power-Percentage": {"icon": "mdi:water-off", "unit": "%"},
    "Ac-General-Power-Percentage": {"icon": "mdi:air-conditioner", "unit": "%"},
    "Outside-Temperature": {"icon": "mdi:thermometer", "unit": "°C"},
    "Outside-Humidity": {"icon": "mdi:water-percent", "unit": "%"},
    "Inside-General-Vpd": {"icon": "mdi:chart-bell-curve", "unit": "kPa"},
    "Inside-General-Temperature-Air": {"icon": "mdi:thermometer", "unit": "°C"},
    "Inside-General-Temperature-Leaf": {"icon": "mdi:leaf", "unit": "°C"},
    "Inside-General-Humidity": {"icon": "mdi:water-percent", "unit": "%"},
    "Inside-General-Co2": {"icon": "mdi:molecule-co2", "unit": "ppm"},
    "Vpd-Min-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "kPa"},
    "Vpd-Min-Value": {"icon": "mdi:arrow-down", "unit": "kPa"},
    "Vpd-Target-Min-Value": {"icon": "mdi:target", "unit": "kPa"},
    "Vpd-Target-Value": {"icon": "mdi:target-variant", "unit": "kPa"},
    "Vpd-Target-Max-Value": {"icon": "mdi:target", "unit": "kPa"},
    "Vpd-Max-Value": {"icon": "mdi:arrow-up", "unit": "kPa"},
    "Vpd-Max-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "kPa"},
    "Temperature-Air-Min-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "°C"},
    "Temperature-Air-Min-Value": {"icon": "mdi:arrow-down", "unit": "°C"},
    "Temperature-Air-Target-Min-Value": {"icon": "mdi:target", "unit": "°C"},
    "Temperature-Air-Target-Value": {"icon": "mdi:target-variant", "unit": "°C"},
    "Temperature-Air-Target-Max-Value": {"icon": "mdi:target", "unit": "°C"},
    "Temperature-Air-Max-Value": {"icon": "mdi:arrow-up", "unit": "°C"},
    "Temperature-Air-Max-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "°C"},
    "Humidity-Min-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "%"},
    "Humidity-Min-Value": {"icon": "mdi:arrow-down", "unit": "%"},
    "Humidity-Target-Min-Value": {"icon": "mdi:target", "unit": "%"},
    "Humidity-Target-Value": {"icon": "mdi:target-variant", "unit": "%"},
    "Humidity-Target-Max-Value": {"icon": "mdi:target", "unit": "%"},
    "Humidity-Max-Value": {"icon": "mdi:arrow-up", "unit": "%"},
    "Humidity-Max-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "%"},    
    "Co2-Min-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "ppm"},
    "Co2-Min-Value": {"icon": "mdi:arrow-down", "unit": "ppm"},
    "Co2-Target-Min-Value": {"icon": "mdi:target", "unit": "ppm"},
    "Co2-Target-Value": {"icon": "mdi:target-variant", "unit": "ppm"},
    "Co2-Target-Max-Value": {"icon": "mdi:target", "unit": "ppm"},
    "Co2-Max-Value": {"icon": "mdi:arrow-up", "unit": "ppm"},
    "Co2-Max-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "ppm"},
    "Soil-Moisture-Min-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "%"},
    "Soil-Moisture-Min-Value": {"icon": "mdi:arrow-down", "unit": "%"},
    "Soil-Moisture-Target-Min-Value": {"icon": "mdi:target", "unit": "%"},
    "Soil-Moisture-Target-Value": {"icon": "mdi:target-variant", "unit": "%"},
    "Soil-Moisture-Target-Max-Value": {"icon": "mdi:target", "unit": "%"},
    "Soil-Moisture-Max-Value": {"icon": "mdi:arrow-up", "unit": "%"},
    "Soil-Moisture-Max-Notification-Value": {"icon": "mdi:bell-alert-outline", "unit": "%"},
    "Vpd-Average-Short-Term": {"icon": "mdi:chart-timeline-variant", "unit": "kPa"},
    "Vpd-Average-Mid-Term": {"icon": "mdi:chart-timeline-variant-shimmer", "unit": "kPa"},
    "Vpd-Average-Long-Term": {"icon": "mdi:chart-timeline", "unit": "kPa"},
    "Temperature-Air-Average-Short-Term": {"icon": "mdi:thermometer", "unit": "°C"},
    "Temperature-Air-Average-Mid-Term": {"icon": "mdi:thermometer", "unit": "°C"},
    "Temperature-Air-Average-Long-Term": {"icon": "mdi:thermometer", "unit": "°C"},
    "Humidity-Average-Short-Term": {"icon": "mdi:water-percent", "unit": "%"},
    "Humidity-Average-Mid-Term": {"icon": "mdi:water-percent", "unit": "%"},
    "Humidity-Average-Long-Term": {"icon": "mdi:water-percent", "unit": "%"},
    "Co2-Average-Short-Term": {"icon": "mdi:molecule-co2", "unit": "ppm"},
    "Co2-Average-Mid-Term": {"icon": "mdi:molecule-co2", "unit": "ppm"},
    "Co2-Average-Long-Term": {"icon": "mdi:molecule-co2", "unit": "ppm"},
    "Soil-Moisture-Average-Short-Term": {"icon": "mdi:water", "unit": "%"},
    "Soil-Moisture-Average-Mid-Term": {"icon": "mdi:water", "unit": "%"},
    "Soil-Moisture-Average-Long-Term": {"icon": "mdi:water", "unit": "%"},
    "Data-Climate-Control": {"icon": "mdi:database"},
    "Data-Light-Control": {"icon": "mdi:database"},
    "Data-Vpd": {"icon": "mdi:database"},
    "Data-Temperature-Air": {"icon": "mdi:database"},
    "Data-Temperature-Leaf": {"icon": "mdi:database"},
    "Data-Humidity": {"icon": "mdi:database"},
    "Data-Co2": {"icon": "mdi:database"},
    "Data-Soil-Moisture": {"icon": "mdi:database"},
    "State-Light": {"icon": "mdi:lightbulb"},
    "State-Exhaust": {"icon": "mdi:fan"},
    "State-Ventilation": {"icon": "mdi:air-filter"},
    "State-Heater": {"icon": "mdi:radiator"},
    "State-Humidifier": {"icon": "mdi:water"},
    "State-Dehumidifier": {"icon": "mdi:water-off"},
    "State-Ac": {"icon": "mdi:air-conditioner"}
}

AREA_BINARY_SENSOR_PARAMETERS = {
    "Area-Is-Day": {"icon": "mdi:weather-sunny","default": False},
    "Debugging-Climate-Control-Data": {"icon": "mdi:bug-outline","default": False},
    "Debugging-Climate-Control-Trends": {"icon": "mdi:chart-line","default": False},
    "Debugging-Climate-Control-States": {"icon": "mdi:state-machine","default": False},
    "Debugging-Climate-Control-Notifications": {"icon": "mdi:bell-alert-outline","default": False},
    "Debugging-Climate-Control-Tasks-Dimming": {"icon": "mdi:lightbulb-auto","default": False},
    "Debugging-Climate-Control-Room-Comparision": {"icon": "mdi:home-analytics","default": False},
    "Debugging-Climate-Control-Tasks-General": {"icon": "mdi:clipboard-list-outline","default": False},
    "Debugging-Climate-Control-Tasks-Check": {"icon": "mdi:check-decagram","default": False}
}

AREA_DATE_PARAMETERS = {
    "Grow-Start-Date": {"icon": "mdi:calendar-start","is_date": True,"is_time": False},
    "Bloom-Start-Date": {"icon": "mdi:calendar-start","is_date": True,"is_time": False},
    "Dry-Start-Date": {"icon": "mdi:calendar-start","is_date": True,"is_time": False},
    "Sunsire-Timestamp": {"icon": "mdi:weather-sunset-up","is_date": True,"is_time": True},
    "Sunset-Timestamp": {"icon": "mdi:weather-sunset-down","is_date": True,"is_time": True}
}
