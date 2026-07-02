# Uni Bremen MQTT Connector Home Assistant App

This Home Assistant App sends specified states collected by Home Assistant to a configured MQTT Broker. It is intended to collect data from demonstrators in research projects by the [working groug Optimization and Optimal Control](https://www.math.uni-bremen.de/zetem/cms/detail.php?id=4381&language=en). 

---

## Installation

1. Navigate to **Settings → Add-ons → Add-on Store** in your Home Assistant.
2. Add this repository to your Home Assistant add-on store:
   - Click the menu (three dots) → _Repositories_
   - Add the repository URL of this project
3. Find **Uni Bremen MQTT Connector** in the add-on list and install it.

---

## Configuration

The App reads the configuration from the file `ha_exporter.json5` in the App 
configuration directory. An example configuration is provided below. The 
`logging` section is optional.

```
{
   "mqtt": {
      "host": "localhost",
      "port": 1883,
      "demonstrator_id": "HA_00000000",
      "api_key": "0123456789abcdef0123456789abcdef"
   },
   "devices": [
      {
         "type": "power_meter",
         "name": "main_power_meter",
         "value_mappings": [
            { "entity": "sensor.power_meter_consumption", "unit": "kWh", "mqtt_name": "total_imported" },
            { "entity": "sensor.power_meter_exported", "unit": "kWh", "mqtt_name": "total_exported" },
            { "entity": "sensor.power_meter_active_power", "unit": "W", "mqtt_name": "power" }
         ]
      },
   ],
   "logging": {
      "version": 1,
      "formatters": {
         "simple_formatter": {"format": "[{asctime}] [{name} {funcName}] [{levelname}]: {message}", "style": "{"}
      },
      "handlers": {
         "simple_handler": { "class":"logging.StreamHandler", "formatter": "simple_formatter", "level": "DEBUG" },
      },
      "loggers": {
         "" : { "handlers": ["simple_handler"], "level": "INFO" },
         "uhb.ha-mqtt-connector": { "level": "DEBUG"},
      }

   }
}

```

---

## License

```
Uni Bremen MQTT Connector Home Assistant App
Copyright (C) 2026  Kevin Holm

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
