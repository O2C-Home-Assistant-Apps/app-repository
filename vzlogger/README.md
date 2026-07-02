# Home Assistant Add-on: vzlogger

> **Disclaimer**
> This add-on is **not** an official project of [volkszaehler.org](https://volkszaehler.org).
> For help with configuring vzlogger go to the official documentation.

---

## About

[vzlogger](https://github.com/volkszaehler/vzlogger) is a command-line data collector for smart meters and other energy measurement devices.
It reads meter data and publishes it to middleware like volkszaehler.org or MQTT.

This Home Assistant add-on packages **vzlogger** for easy deployment and integration within Home Assistant.

---

## Usage

1. Navigate to **Settings → Add-ons → Add-on Store** in your Home Assistant.
2. Add this repository to your Home Assistant add-on store:
   - Click the menu (three dots) → _Repositories_
   - Add the repository URL of this project
3. Find **vzlogger** in the add-on list and install it.
4. Follow the [DOCS](vzlogger/DOCS.md) for configuration

## Links

- [vzlogger git repo](https://github.com/volkszaehler/vzlogger)
- [vzlogger homepage](https://wiki.volkszaehler.org/software/controller/vzlogger)

## Supported setups

This Add-on has only been tested on a [Home Assistant Green](https://www.home-assistant.io/green/) with a [USB IR Interface from ELV](https://de.elv.com/p/elv-lesekopf-mit-usb-schnittstelle-fuer-digitale-zaehler-usb-iec-P158713/?itemId=158713). It should work with other IR Interfaces and on other CPU architectures.

## Support

Feel free to contact me at techo2c [at] uni-bremen.de

## Credits

The image produced by the [Dockerfile](vzlogger/Dockerfile) is based on the [base image provided by Home Assistant Community Add-on](https://github.com/hassio-addons/addon-base) a copy of it's license can be found in the [licenses](licenses) directory.

The [Dockerfile](vzlogger/Dockerfile) itself is based on the Dockerfile available in the [vzlogger repository](https://github.com/volkszaehler/vzlogger) modified to use the Home Assistant base image; this repository is licensed under the same GPL-3.0 license, a copy is available in the [LICENSE](LICENSE) file.

## License

Copyright © 2025 Kevin Holm
This Project is licensed under [GPL-3.0](LICENSE).
