import os

# MQTT Broker Settings
MQTT_HOST = os.getenv("MQTT_HOST", "homeassistant.local")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "")

# Client details
CLIENT_ID = os.getenv("MQTT_CLIENT_ID", "rpi_relay_controller")
DEVICE_NAME = "FloraFlow"
DEVICE_MODEL = "Raspberry Pi Zero W"
DEVICE_MANUFACTURER = "Custom Integration"
DEVICE_ID = "floraflow"


# Home Assistant Discovery Configuration
DISCOVERY_PREFIX = os.getenv("MQTT_DISCOVERY_PREFIX", "homeassistant")

# Relay Configuration
RELAY_PINS = [5, 6, 13, 19, 26, 16, 20, 21]

# Set to True for Active-Low relays (common 5V 8-channel relay boards turn ON when pin is pulled LOW)
# Set to False for Active-High relays (turn ON when pin is driven HIGH)
ACTIVE_LOW = True

# Persistence setting
PERSISTENCE_FILE = os.getenv("PERSISTENCE_FILE", "schedules.json")

# Heartbeat interval in seconds
HEARTBEAT_INTERVAL = 30

# DHT22 Configuration
DHT_PIN = int(os.getenv("DHT_PIN", 4))
DHT_INTERVAL = int(os.getenv("DHT_INTERVAL", 60))
