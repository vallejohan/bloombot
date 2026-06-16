import json
import logging

import paho.mqtt.client as mqtt

import config

logger = logging.getLogger(__name__)


class MQTTHandler:
    """Handles MQTT connection, Home Assistant discovery, and state/command communication."""

    def __init__(
        self,
        on_relay_toggle,
        on_schedule_toggle,
        on_start_time_change,
        on_duration_change,
    ):

        self.client = None
        self.connected = False

        # Callbacks
        self.on_relay_toggle = on_relay_toggle
        self.on_schedule_toggle = on_schedule_toggle
        self.on_start_time_change = on_start_time_change
        self.on_duration_change = on_duration_change

    def connect(self):
        """Initialize and connect the MQTT client."""
        logger.info(
            f"Connecting to MQTT Broker {config.MQTT_HOST}:{config.MQTT_PORT}..."
        )
        self.client = mqtt.Client(client_id=config.CLIENT_ID)

        # Configure username and password if provided
        if config.MQTT_USERNAME:
            self.client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)

        # Set Last Will and Testament (LWT)
        availability_topic = f"garden/availability"
        self.client.will_set(availability_topic, payload="offline", qos=1, retain=True)

        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_message = self._on_message

        try:
            self.client.connect(config.MQTT_HOST, config.MQTT_PORT, keepalive=60)
            self.client.loop_start()
        except Exception as e:
            logger.error(f"MQTT connection failed: {e}")

    def disconnect(self):
        """Disconnect the MQTT client."""
        if self.client:
            logger.info("Disconnecting MQTT client...")
            # Publish offline before disconnecting cleanly
            self.client.publish("garden/availability", "offline", retain=True)
            self.client.loop_stop()
            self.client.disconnect()

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("MQTT client connected successfully.")
            self.connected = True

            # Publish birth message (online availability)
            self.client.publish("garden/availability", "online", retain=True)

            # Subscribe to all command topics
            # garden/relay/+/set (Manual Relay State Control)
            # garden/relay/+/schedule/set (Schedule Enabled Toggle)
            # garden/relay/+/start_time/set (Schedule Start Time)
            # garden/relay/+/duration/set (Schedule Duration)
            self.client.subscribe("garden/relay/+/set", qos=1)
            self.client.subscribe("garden/relay/+/schedule/set", qos=1)
            self.client.subscribe("garden/relay/+/start_time/set", qos=1)
            self.client.subscribe("garden/relay/+/duration/set", qos=1)

            # Register Home Assistant entities via Auto-Discovery
            self.publish_discovery()
        else:
            logger.error(f"MQTT connection failed with code {rc}")

    def _on_disconnect(self, client, userdata, rc):
        logger.warning(f"MQTT client disconnected. Code: {rc}")
        self.connected = False

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode("utf-8").strip()
        logger.debug(f"Received message on {topic}: {payload}")

        try:
            parts = topic.split("/")
            # Expected topic formats:
            # 1. garden/relay/<relay_num>/set
            # 2. garden/relay/<relay_num>/schedule/set
            # 3. garden/relay/<relay_num>/start_time/set
            # 4. garden/relay/<relay_num>/duration/set

            if len(parts) < 4:
                return

            relay_num = int(parts[2])
            if relay_num < 1 or relay_num > len(config.RELAY_PINS):
                logger.warning(f"Invalid relay index in topic: {topic}")
                return

            action_type = parts[3]

            if action_type == "set":
                # Manual toggle command
                state = payload.upper() == "ON"
                self.on_relay_toggle(relay_num, state)

            elif action_type == "schedule" and len(parts) == 5 and parts[4] == "set":
                # Schedule enabled command
                enabled = payload.upper() == "ON"
                self.on_schedule_toggle(relay_num, enabled)

            elif action_type == "start_time" and parts[4] == "set":
                # Start time command (expected "HH:MM:SS" or "HH:MM")
                self.on_start_time_change(relay_num, payload)

            elif action_type == "duration" and parts[4] == "set":
                # Duration command (expected integer in minutes)
                duration = int(float(payload))
                self.on_duration_change(relay_num, duration)

        except Exception as e:
            logger.error(f"Error handling message on {topic}: {e}")

    def publish_discovery(self):
        """Publish discovery configurations for all 8 relays to Home Assistant."""
        logger.info("Publishing Home Assistant Auto-Discovery configs...")

        device_info = {
            "identifiers": [config.DEVICE_ID],
            "name": config.DEVICE_NAME,
            "model": config.DEVICE_MODEL,
            "manufacturer": config.DEVICE_MANUFACTURER,
            "sw_version": "1.0.0",
        }

        availability_topic = f"garden/availability"

        for i in range(1, len(config.RELAY_PINS) + 1):
            base_node = f"relay_{i}"

            # 1. Manual Relay Switch
            relay_config = {
                "name": f"Relay {i}",
                "unique_id": f"{config.DEVICE_ID}_relay_{i}",
                "state_topic": f"garden/relay/{i}/state",
                "command_topic": f"garden/relay/{i}/set",
                "payload_on": "ON",
                "payload_off": "OFF",
                "availability_topic": availability_topic,
                "device": device_info,
                "icon": "mdi:water-pump",
                "has_entity_name": True,
            }
            self.client.publish(
                f"{config.DISCOVERY_PREFIX}/switch/{config.DEVICE_ID}/relay_{i}/config",
                payload=json.dumps(relay_config),
                qos=1,
                retain=True,
            )

            # 2. Schedule Enabled Switch
            schedule_config = {
                "name": f"Relay {i} Schedule Enabled",
                "unique_id": f"{config.DEVICE_ID}_relay_{i}_schedule_enabled",
                "state_topic": f"garden/relay/{i}/schedule/state",
                "command_topic": f"garden/relay/{i}/schedule/set",
                "payload_on": "ON",
                "payload_off": "OFF",
                "availability_topic": availability_topic,
                "device": device_info,
                "icon": "mdi:calendar-clock",
                "has_entity_name": True,
            }
            self.client.publish(
                f"{config.DISCOVERY_PREFIX}/switch/{config.DEVICE_ID}/relay_{i}_schedule/config",
                payload=json.dumps(schedule_config),
                qos=1,
                retain=True,
            )

            # 3. Schedule Start Time (Time Picker)
            start_time_config = {
                "name": f"Relay {i} Start Time",
                "unique_id": f"{config.DEVICE_ID}_relay_{i}_start_time",
                "state_topic": f"garden/relay/{i}/start_time/state",
                "command_topic": f"garden/relay/{i}/start_time/set",
                "availability_topic": availability_topic,
                "device": device_info,
                "icon": "mdi:clock-start",
                "has_entity_name": True,
            }
            self.client.publish(
                f"{config.DISCOVERY_PREFIX}/time/{config.DEVICE_ID}/relay_{i}_start_time/config",
                payload=json.dumps(start_time_config),
                qos=1,
                retain=True,
            )

            # 4. Schedule Duration (Number Input/Slider)
            duration_config = {
                "name": f"Relay {i} Duration",
                "unique_id": f"{config.DEVICE_ID}_relay_{i}_duration",
                "state_topic": f"garden/relay/{i}/duration/state",
                "command_topic": f"garden/relay/{i}/duration/set",
                "min": 1,
                "max": 180,
                "step": 1,
                "unit_of_measurement": "min",
                "mode": "slider",
                "availability_topic": availability_topic,
                "device": device_info,
                "icon": "mdi:timer-outline",
                "has_entity_name": True,
            }
            self.client.publish(
                f"{config.DISCOVERY_PREFIX}/number/{config.DEVICE_ID}/relay_{i}_duration/config",
                payload=json.dumps(duration_config),
                qos=1,
                retain=True,
            )

        # 5. Temperature Sensor
        temp_config = {
            "name": "Temperature",
            "unique_id": f"{config.DEVICE_ID}_temperature",
            "state_topic": "garden/sensor/temperature",
            "unit_of_measurement": "°C",
            "device_class": "temperature",
            "state_class": "measurement",
            "availability_topic": availability_topic,
            "device": device_info,
            "has_entity_name": True,
        }
        self.client.publish(
            f"{config.DISCOVERY_PREFIX}/sensor/{config.DEVICE_ID}/temperature/config",
            payload=json.dumps(temp_config),
            qos=1,
            retain=True,
        )

        # 6. Humidity Sensor
        humidity_config = {
            "name": "Humidity",
            "unique_id": f"{config.DEVICE_ID}_humidity",
            "state_topic": "garden/sensor/humidity",
            "unit_of_measurement": "%",
            "device_class": "humidity",
            "state_class": "measurement",
            "availability_topic": availability_topic,
            "device": device_info,
            "has_entity_name": True,
        }
        self.client.publish(
            f"{config.DISCOVERY_PREFIX}/sensor/{config.DEVICE_ID}/humidity/config",
            payload=json.dumps(humidity_config),
            qos=1,
            retain=True,
        )

    def publish_sensor_data(self, temperature, humidity):
        """Publish DHT22 temperature and humidity sensor readings to Home Assistant."""
        if self.client and self.connected:
            if temperature is not None:
                self.client.publish(
                    "garden/sensor/temperature", str(temperature), qos=1, retain=True
                )
                logger.info(f"Published temperature: {temperature}°C")
            if humidity is not None:
                self.client.publish(
                    "garden/sensor/humidity", str(humidity), qos=1, retain=True
                )
                logger.info(f"Published humidity: {humidity}%")

    def publish_relay_state(self, relay_num, state: bool):
        """Publish the physical relay state (ON/OFF) to HA."""
        topic = f"garden/relay/{relay_num}/state"
        payload = "ON" if state else "OFF"
        if self.client and self.connected:
            self.client.publish(topic, payload, qos=1, retain=True)

    def publish_schedule_enabled(self, relay_num, enabled: bool):
        """Publish the schedule enabled state (ON/OFF) to HA."""
        topic = f"garden/relay/{relay_num}/schedule/state"
        payload = "ON" if enabled else "OFF"
        if self.client and self.connected:
            self.client.publish(topic, payload, qos=1, retain=True)

    def publish_start_time(self, relay_num, time_str):
        """Publish the schedule start time (HH:MM:SS) to HA."""
        topic = f"garden/relay/{relay_num}/start_time/state"
        if self.client and self.connected:
            # Home Assistant expects format "HH:MM:SS" or "HH:MM"
            self.client.publish(topic, time_str, qos=1, retain=True)

    def publish_duration(self, relay_num, duration: int):
        """Publish the schedule duration (minutes) to HA."""
        topic = f"garden/relay/{relay_num}/duration/state"
        if self.client and self.connected:
            self.client.publish(topic, str(duration), qos=1, retain=True)

    def publish_heartbeat(self):
        """Publish periodic online availability message."""
        if self.client and self.connected:
            self.client.publish("garden/availability", "online", qos=1, retain=True)
            logger.debug("Heartbeat published.")
