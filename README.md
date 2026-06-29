<p align="center">
  <img src="/img/floraflow-logo.png" width="200"/>
</p>

<h1 align="center">FloraFlow</h1>

<p align="center">
  <strong>A lightweight irrigation controller.</strong><br>
  Using a Raspberry Pi, with home assistant integration.
</p>

<p align="center">
  <a href="https://github.com/vallejohan/floraflow/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="MIT License" />
  </a>
</p>

---

## What is FloraFlow?
A lightweight garden and greenhouse irrigation controller running on a **Raspberry Pi Zero W** (or any other Raspberry Pi) to control a 5V relay board. It integrates with **Home Assistant** over **MQTT** using automatic discovery, and supports both scheduled watering (by time-of-day and duration) and manual overrides.

## Features

- **Multi-Channel Relay Control:** Toggle individual water valves/relays on physical GPIO pins.
- **Humidity & temperature measurement:** Measure the humidity and temperature in the garden/greenhouse using an appropriate sensor (such as DHT22 or a DHT11).
- **Home Assistant Auto-Discovery:** No manual YAML configuration required in Home Assistant. Switches, schedule toggles, start times, and watering durations register automatically.
- **Persistent Schedules:** Schedules are stored locally in `schedules.json` so that they survive Raspberry Pi reboots or power cycles.
- **Flexible Timing:** Set the start time (HH:MM:SS) and duration (1 to 10 minutes) for each relay.
- **Safety Auto-Shutoff:** If the scheduler triggers a relay, it automatically shuts off after the configured duration. If a manual OFF override is received during watering, the timer is immediately cancelled.
- **GPIO Fallback & Mocking:** Automatically detects the physical `gpiozero` library. If run on a non-Pi machine (like Windows/Mac for testing), it runs in **Mock mode** allowing you to test Home Assistant communications.

---

## Hardware Setup
The hardware consists of a Raspberry Pi Zero W, 8-channel relay board, humidity and temperature sensor (DHT22), water valves, and a home assistant server. It's fully possible to pick any number of relays to control (as long as there are available GPIO pins on the Raspberry Pi), since the number of relays are configured in [config.py](src/config.py). The flowchart below illustrates a rough overview of how the various hardware (and software) are connected. The power source is from an 230V outlet, which has a 230V-12V switched power supply inbetween to get the correct voltage for the 12V water valves. For the Raspberry Pi and relay board there is an additional 12V-5V DC converter to get the correct voltage.

One thing that is good to mention is the water source and water valve, since these can change depending on your conditions. Some might have a water barrel available instead of a water faucet that can contiuosly supply water. In this case the usage of water pumps would work just as well.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/img/floraflow-flowchart-dark-theme.png">
  <img alt="FloraFlow Architecture Diagram" src="/img/floraflow-flowchart-light-theme.png">
</picture>


### Wiring

The default GPIO pin connections used to control the relays are defined in [config.py](src/config.py):

| Relay Channel | GPIO Pin | Connection Notes |
| :---: | :---: | :--- |
| **Relay 1** | GPIO 5 | Valve / Zone 1 |
| **Relay 2** | GPIO 6 | Valve / Zone 2 |
| **Relay 3** | GPIO 13 | Valve / Zone 3 |
| **Relay 4** | GPIO 16 | Valve / Zone 4 |
| **Relay 5** | GPIO 19 | Valve / Zone 5 |
| **Relay 6** | GPIO 20 | Valve / Zone 6 |
| **Relay 7** | GPIO 21 | Valve / Zone 7 |
| **Relay 8** | GPIO 26 | Valve / Zone 8 |

- **Active-Low vs. Active-High:** Most common 8-channel relay boards are *Active-Low* (relays switch ON when the control pin is pulled to GND). This is configured via `ACTIVE_LOW = True` in [config.py](src/config.py).
- **Isolation (JD-VCC):** To isolate the Raspberry Pi from relay noise and ensure the 5V relay coils have sufficient power, remove the VCC/JD-VCC jumper on the relay board:
  - Connect **JD-VCC** to an external 5V power supply's positive terminal.
  - Connect **GND** of the external power supply to the relay board GND (and keep it isolated from the Pi GND if you want full opto-isolation).
  - Connect **VCC** on the relay board to the Pi's **3.3V pin** (so the optocouplers are driven by the Pi's 3.3V logic).

---

## Limitations & Considerations

Before starting the setup of this project there are some limitations with this hardware that are good to consider: 

- **WiFi Range Outdoors:** The onboard PCB antenna of the Raspberry Pi Zero W has limited range, which is further reduced when placed inside a weatherproof enclosure. If the Pi is far from your router, you may experience intermittent MQTT disconnections.
   * *Tip:* Consider placing a WiFi extender closer to the garden, or using a Raspberry Pi model with an external antenna connector.
- **Power Consumption:** Unlike low-power microcontrollers (such as the ESP32) which can enter deep-sleep mode and draw microamps, a Raspberry Pi Zero W consumes quite substantially more power.
  * *Tip:* Running FloraFlow purely on batteries is impractical unless you plan for a substantial solar panel setup (e.g., 10W+ solar panel, 12V LiFePO4 battery, and a step-down converter). A mains-powered supply is highly recommended.
- **No Native Analog Inputs:** The Raspberry Pi lacks analog-to-digital converters (ADC). 
   * *Tip:* If you plan to expand the hardware to read analog soil moisture sensors, you will need to add an external ADC chip.

> [!NOTE]
> **Design Philosophy & Hardware Selection**
> 
> This project was originally planned around an ESP32 microcontroller. While an ESP32 would be more optimal on several fronts, such as low power consumption, native ADC support, and support for wireless protocols like Zigbee or Thread, a Raspberry Pi was chosen for a few key reasons:
> - **Power & Proximity:** The greenhouse is close to the main house with a direct power line, which minimizes power consumption constraints.
> - **Extensibility & Easy Updates:** Running a full Linux environment allows for trivial Over-the-Air (OTA) updates and leaves the door open to run other companion services on the same device in the future.
> - **Hardware Reuse:** It was a good opportunity to put a spare Raspberry Pi board I had lying around to good use.

---

## Installation & Setup on Raspberry Pi

### 1. Install System Dependencies

Open a terminal on your Raspberry Pi and ensure all required system utilities and build tools are installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv python3-gpiozero swig liblgpio-dev python3-dev build-essential
```

> [!NOTE]
> * **Relay Control:** On modern Debian/Ubuntu environments (such as RPi OS Bookworm), legacy GPIO interfaces are deprecated. To control pins correctly, the application compiles `lgpio` in the virtual environment via the modern `/dev/gpiochip*` API, requiring the compilation dependencies (`swig`, `liblgpio-dev`, `python3-dev`, `build-essential`).

### 2. Clone and Prepare the Script

First, install **uv** if it isn't already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Navigate to your workspace directory and synchronize the dependencies to set up a virtual environment:

```bash
cd /path/to/your/workspace/floraflow
uv sync
```

### 3. Enable Linux Kernel DHT Overlay (Required for DHT22 Sensor)

Python-based user-space bit-banging is highly sensitive to CPU scheduling jitter (especially on single-core devices like the Raspberry Pi Zero W). To achieve stable readings, this application relies on the built-in **Linux Kernel Driver**. The kernel handles timing-sensitive pulse measurements asynchronously via hardware interrupts.

To enable the kernel driver:

1. Open the Raspberry Pi firmware configuration file:
   ```bash
   sudo nano /boot/firmware/config.txt
   ```
2. Scroll to the bottom of the file and add the following lines (under the `[all]` block if present):
   ```text
   [all]
   dtoverlay=dht11,dht22,gpiopin=4
   ```
3. Save the file and reboot your Raspberry Pi:
   ```bash
   sudo reboot
   ```

### 4. Configuration

To configure FloraFlow, you can copy the `.env.example` template to `.env` and adjust the variables to fit your network and system:

```bash
cp .env.example .env
```

Open `.env` and set the parameters:
- `MQTT_HOST`: Set your Home Assistant broker IP (defaults to `homeassistant.local`).
- `MQTT_PORT`: Port of the broker (defaults to `1883`).
- `MQTT_USERNAME` / `MQTT_PASSWORD`: MQTT broker login credentials if enabled.
- `MQTT_CLIENT_ID`: The client ID for the MQTT connection (defaults to `rpi_relay_controller`).
- `PERSISTENCE_FILE`: File name to save schedules (defaults to `schedules.json`).
- `DHT_PIN`: BCM pin number connected to the DHT sensor (defaults to `4`).
- `DHT_INTERVAL`: Sensor reading and publishing frequency in seconds (defaults to `60`).

*Note: For properties like `ACTIVE_LOW` and `RELAY_PINS`, you can modify their default values directly in [config.py](src/config.py).*

---

## Running the Daemon

### Running Manually (Testing/Development)

You can run the daemon manually to verify the MQTT broker connection and check the terminal log outputs:

```bash
uv run python src/main.py
```

### Running as a Persistent System Service (`systemd`)

To run the daemon automatically when the Pi boots and ensure it restarts on crashes:

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/floraflow.service
   ```

2. Paste the following configuration (replace paths and users with your actual Pi configuration):
   ```ini
   [Unit]
   Description=FloraFlow Irrigation Controller Daemon
   After=network.target mqtt.service

   [Service]
   Type=simple
   User=pi
   WorkingDirectory=/home/pi/floraflow
   ExecStart=/home/pi/floraflow/.venv/bin/python src/main.py
   Restart=always
   RestartSec=5

   [Install]
   WantedBy=multi-user.target
   ```

   *(Note: The daemon will automatically load the configuration variables from the `.env` file located in the configured `WorkingDirectory`.)*

3. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable floraflow.service
   sudo systemctl start floraflow.service
   ```

4. View service logs to monitor execution:
   ```bash
   sudo journalctl -u floraflow.service -f
   ```

---

## Testing in Mock Mode (Without a Raspberry Pi)

If you are developing or testing on a laptop/desktop computer (e.g. Windows/Mac):

1. Synchronize the environment:
   ```bash
   uv sync
   ```
2. Run the application:
   ```bash
   uv run python src/main.py
   ```
3. The daemon will print `[GPIO-MOCK]` lines showing what the physical pins *would* be doing when you toggle switches in Home Assistant.
4. Use **MQTT Explorer** or the Home Assistant developer tools to verify that entities publish their states and commands are received correctly.

---

## Home Assistant Dashboard Setup

This project includes a Lovelace card designed to control scheduled and manual irrigation valves with configuration dialogs.

### Installation via HACS (Home Assistant Community Store)

1. Go to **HACS** in your Home Assistant dashboard.
2. Select **Lovelace** (or search all categories).
3. Search for **FloraFlow Card**.
4. Click **Download** in the bottom right corner.

### Dashboard Configuration

Once installed, you can add the card to your dashboard using the Custom UI card selector. See [garden-relay-card-example.yaml](home-assistant/dashboard-examples/garden-relay-card-example.yaml) for an example on how the card is set up in Home Assistant.

---

## Local Unit Testing & Formatting Checks

To verify code functionality and format compliance locally:

### 1. Run Formatting & Import Checks
FloraFlow uses `isort` and `black` to enforce style guidelines.

To check without modifying files:
```bash
# Check import sort ordering
uv run isort --check src tests

# Check code style formatting
uv run black --check src tests
```

To automatically format the code and sort imports:
```bash
uv run isort .
uv run black .
```

### 2. Run the Unit Test Suite
To run the full suite of tests:
```bash
uv run python -m unittest discover -s tests
```
