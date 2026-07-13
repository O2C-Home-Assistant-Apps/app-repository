# Living Energy

A weather & energy dashboard for Home Assistant. Shows current weather
conditions and live power/energy readings from your own HA entities, with
signed grid export/import display, history sparklines, consumption bar
charts, power analysis (base load, min/max), and a weather forecast.
Light/dark mode and German/English language switch included.

The dashboard runs entirely on local Home Assistant data and sends nothing
externally by default. An optional **data synchronization (opt-in)** can
forward metadata to an external MQTT broker — this is off by default and the
dashboard is fully usable without it. Delivery is handled by the bundled
`uhb-mqtt-connector`, which starts only after you consent and activate transfer.

## Installation

1. In Home Assistant, go to **Settings → Apps** (labelled **"Add-ons"** in
   older Home Assistant versions) **→ App Store**.
2. Open the **⋮** menu (top right) → **Repositories**.
3. Add this repository URL:
   ```
   https://gitlab.informatik.uni-bremen.de/home-assistant/addon-living-energy
   ```
4. Find **Living Energy** in the store and click **Install**.
5. Start the app and open it from the sidebar (Ingress).

> Running Home Assistant in a container instead of HA OS? See the
> repository root `README.md` for a `docker-compose.yml` based setup.

## Configuration

Most settings are managed from the dashboard's own **Settings** page, but
they are also exposed as app options:

| Option | Description |
|---|---|
| `weather_entity` | A `weather.*` entity (current conditions, temperature, humidity, wind). |
| `power_entity` | A sensor with device class `power` (instantaneous consumption in W; negative = solar export). |
| `energy_entity` | A cumulative `energy` sensor for grid consumption/import (kWh). |
| `energy_export_entity` | Optional cumulative `energy` sensor for grid export (kWh). |
| `cost_per_kwh` | Optional electricity price (€/kWh). Enables cost tiles on the dashboard. |
| `annual_basic_price` | Optional fixed annual price component (€/year). |
| `mqtt_opt_in` | Enables external data synchronization (off by default). |
| `mqtt_host` / `mqtt_port` / `mqtt_demonstrator_id` / `mqtt_api_key` | MQTT broker connection details, used only when opted in (`demonstrator_id` = username, `api_key` = password). |

## Privacy

External data synchronization is **opt-in**. While disabled, no metadata
leaves your Home Assistant instance. You can enable or revoke it at any
time from the dashboard's Settings page. See the app's `DOCS.md`
(shown in the Documentation tab) for details.
