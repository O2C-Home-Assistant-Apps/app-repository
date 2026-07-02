# Configuration and Usage

## Device Selection

Before the first startup, you must **select the device** (e.g. `/dev/ttyUSB0`) in the add-on configuration.
Without a device selected the Add-On can not be started, only a single device is passed through for security.

---

## Configuration

### vzlogger.conf

- vzlogger will only start after a valid **`vzlogger.conf`** file exists in
  `/addon_configs/{REPO}_vzlogger/`.\*
- On the **first startup**, an **`vzlogger.conf.example`** file is automatically created in the same directory. You can use it as a template to build your configuration.
- You can rename or copy `vzlogger.conf.example` to `vzlogger.conf` if the [Mosquitto broker Add-On](https://github.com/home-assistant/addons/tree/master/mosquitto) is installed. This will result in random measurments being generated since the meter protocol is set to `random`.

## \*{REPO} is a hash of the repository url. The directory will be automatically created on first startup.

#### Template Support

The `vzlogger.conf` supports limited templating for convenience:

- **Device path**: Auto-filled from the selected device in the add-on configuration.
- **MQTT settings**: If the Home Assistant MQTT Broker add-on is installed and active, the configuration template can automatically include correct broker connection details.

For a usage example, of all available placeholders, look at the [vzlogger.conf.example](rootfs/etc/vzlogger.conf.example).

---

## Log Levels

- **Container startup script log level**: Can be set via the add-on Configuration. This controls the verbosity of the bashio startup and shtudown scripts in the container.
- **vzlogger log level**: Is configured separately inside the `vzlogger.conf` file under the `verbosity` option. For information on available values look in the [official documentation](https://wiki.volkszaehler.org/software/controller/vzlogger/vzlogger_conf_parameter#verbosity)

---

## Integrate sensor in Home Assistant

To add the power meter as a device to Home Assistant the [MQTT Integration](https://www.home-assistant.io/integrations/mqtt/) needs to be installed. Manual configuration of a new MQTT device is required.

To see the messages published by vzlogger follow the ["Testing your setup"](https://www.home-assistant.io/integrations/mqtt/#testing-your-setup) steps to "Listen to a topic", using the topic from the example file the topic to listen to would be `vzlogger/data/#`.

There should be messages visible under a topic like `vzlogger/data/chn0/raw` with messages like:

```json
{ "timestamp": 1752348271769, "value": 50913.538 }
```

Depending on what values the configured power meter provides multiple entities might need to be added. Something that should be available in all power meters is the Total Energy Consumed in kWh. That can be configured following the "ADD MQTT DEVICE" GUI workflow, with the example random data using these settings works: 

```
Type of entity: Sensor
Entity name: power_meter
Device class: Energy
State class: Measurment
Unit of measurement: kWh
State topic: vzlogger/data/chn0/raw
Value template: {{ value_json.value }}
```

Fields not mentioned were left empty. More information on the options can be found in the [MQTT Integration Documentation](https://www.home-assistant.io/integrations/sensor.mqtt/)

---
