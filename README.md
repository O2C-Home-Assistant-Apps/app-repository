# University Bremen - Home Assistant Apps

## About

Home Assistant allows anyone to create app repositories to share their
apps for Home Assistant easily. This repository is one of those repositories,
providing extra Home Assistant apps for your installation.

This repository contains Home Assistant apps created by projects at the
University of Bremen. It is a [mirror](https://gitlab.informatik.uni-bremen.de/home-assistant/app-repository) from the University's GitLab instance.

Use this repository to report all issues encounterd with any of our Apps.

## Installation

The easiest way to add this repository to Home Assistant is to click this 
button:

[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FO2C-Home-Assistant-Apps%2Fapp-repository)

If that dosen't work, the repository can manually be added to Home Assistant
under **Settings -> Apps -> Install app** in the **Repositories** settings 
(hidden in the top right hamburger menu).

Use the following URL to add this repository:

```txt
https://github.com/O2C-Home-Assistant-Apps/app-repository
```

## Apps provided by this repository

### [Living Energy](https://gitlab.informatik.uni-bremen.de/home-assistant/addon-living-energy)

Frontend to visualize Energy usage and transmit states collected by 
Home Assistant to a configured MQTT broker.

### [vzlogger](https://gitlab.informatik.uni-bremen.de/home-assistant/addon-vzlogger)

> [!CAUTION]
> This App is not an official project of volkszaehler.org.
> 
> For help with configuring vzlogger go to the official documentation.

[vzlogger](https://github.com/volkszaehler/vzlogger) packaged as a 
Home Assistant app.

### [UHB MQTT Connector](https://gitlab.informatik.uni-bremen.de/home-assistant/addon-uhb-mqtt-connector)

Backend used by Living Energy to transmit states collected by Home Assistant to
a configured MQTT broker.
