import json
import logging
import os
import signal
import sys
import time

import config
from dht_sensor import DHTSensorManager
from gpio_manager import GPIOManager
from mqtt_handler import MQTTHandler
from scheduler import GardenScheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("Main")


class GardenControllerApp:
    def __init__(self):
        self.schedules = {}
        self.gpio_mgr = None
        self.mqtt_handler = None
        self.scheduler = None
        self.dht_sensor = None
        self.last_dht_read_time = 0
        self.running = False
        self.num_relays = self.count_relays()

        self.load_schedules()

    def count_relays(self):
        if len(config.RELAY_PINS) == 0:
            logger.error("No relay pins configured!")
            sys.exit(1)
        return len(config.RELAY_PINS)

    def load_schedules(self):
        """Load schedules from schedules.json, or initialize with defaults if not found."""
        if os.path.exists(config.PERSISTENCE_FILE):
            try:
                with open(config.PERSISTENCE_FILE, "r") as f:
                    self.schedules = json.load(f)
                logger.info(f"Loaded existing schedules from {config.PERSISTENCE_FILE}")
            except Exception as e:
                logger.error(
                    f"Error loading {config.PERSISTENCE_FILE}: {e}. Initializing defaults."
                )
                self.initialize_default_schedules()
        else:
            logger.info("No schedules file found. Initializing defaults.")
            self.initialize_default_schedules()

        # Ensure all relays exist in schedules
        for i in range(1, self.num_relays + 1):
            key = f"relay_{i}"
            if key not in self.schedules:
                self.schedules[key] = {
                    "schedule_enabled": False,
                    "start_times": [{"time": "08:00:00", "enabled": True}],
                    "duration": 10,
                }
            else:
                sched = self.schedules[key]
                if "start_times" not in sched:
                    sched["start_times"] = [{"time": "08:00:00", "enabled": True}]
        self.save_schedules()

    def initialize_default_schedules(self):
        """Create a default schedule configuration for all relays."""
        self.schedules = {}
        for i in range(1, self.num_relays + 1):
            self.schedules[f"relay_{i}"] = {
                "schedule_enabled": False,
                "start_times": [{"time": "08:00:00", "enabled": True}],
                "duration": 10,
            }

    def save_schedules(self):
        """Write current schedules to schedules.json file."""
        try:
            with open(config.PERSISTENCE_FILE, "w") as f:
                json.dump(self.schedules, f, indent=4)
            logger.debug("Schedules saved to file.")
        except Exception as e:
            logger.error(f"Failed to save schedules: {e}")

    def on_relay_toggle(self, relay_num, state):
        """Callback for manual relay toggle from MQTT."""
        logger.info(
            f"Manual override command received: Relay {relay_num} -> {'ON' if state else 'OFF'}"
        )

        if state:
            self.gpio_mgr.turn_on(relay_num)
        else:
            self.gpio_mgr.turn_off(relay_num)
            self.scheduler.cancel_active_run(relay_num)

        self.mqtt_handler.publish_relay_state(relay_num, state)

    def on_schedule_toggle(self, relay_num, enabled):
        """Callback for schedule enabled state change."""
        key = f"relay_{relay_num}"
        logger.info(
            f"Schedule toggle command received: Relay {relay_num} schedule -> {'ENABLED' if enabled else 'DISABLED'}"
        )

        self.schedules[key]["schedule_enabled"] = enabled
        self.save_schedules()

        self.mqtt_handler.publish_schedule_enabled(relay_num, enabled)

    def on_start_times_change(self, relay_num, payload_str):
        """Callback for schedule start times JSON change."""
        try:
            items = json.loads(payload_str)
            if not isinstance(items, list) or len(items) == 0:
                raise ValueError("Start times must be a non-empty list")

            valid_items = []
            for item in items:
                if not isinstance(item, dict) or "time" not in item:
                    continue
                time_str = item["time"].strip()
                # Validate format (expect HH:MM or HH:MM:SS)
                parts = time_str.split(":")
                if len(parts) in (2, 3):
                    h = int(parts[0])
                    m = int(parts[1])
                    if 0 <= h < 24 and 0 <= m < 60:
                        if len(parts) == 2:
                            time_str = f"{h:02d}:{m:02d}:00"
                        enabled = bool(item.get("enabled", False))
                        valid_items.append({"time": time_str, "enabled": enabled})

            if len(valid_items) == 0:
                raise ValueError("No valid start times provided")

            key = f"relay_{relay_num}"
            logger.info(
                f"Schedule start times change: Relay {relay_num} -> {valid_items}"
            )
            self.schedules[key]["start_times"] = valid_items
            self.save_schedules()

            self.mqtt_handler.publish_start_times(relay_num, valid_items)

        except Exception as e:
            logger.error(
                f"Invalid start times payload received for relay {relay_num}: {payload_str}. Error: {e}"
            )
            key = f"relay_{relay_num}"
            self.mqtt_handler.publish_start_times(
                relay_num, self.schedules[key]["start_times"]
            )

    def on_duration_change(self, relay_num, duration):
        """Callback for schedule watering duration change."""
        key = f"relay_{relay_num}"
        duration = max(1, min(10, duration))
        logger.info(
            f"Schedule duration change: Relay {relay_num} -> {duration} minutes"
        )

        self.schedules[key]["duration"] = duration
        self.save_schedules()

        self.mqtt_handler.publish_duration(relay_num, duration)

    def toggle_relay_from_scheduler(self, relay_num, state, is_scheduled=True):
        """Callback invoked by the scheduler when it starts or stops watering."""
        logger.info(
            f"[SCHEDULER ACTION] Relay {relay_num} -> {'ON' if state else 'OFF'}"
        )

        if state:
            self.gpio_mgr.turn_on(relay_num)
        else:
            self.gpio_mgr.turn_off(relay_num)

        self.mqtt_handler.publish_relay_state(relay_num, state)

    def publish_initial_states(self):
        """Publish current system configurations and relay states to Home Assistant."""
        logger.info("Synchronizing initial state with Home Assistant...")
        for i in range(1, self.num_relays + 1):
            key = f"relay_{i}"
            sched = self.schedules[key]

            # Initial relay state is OFF when daemon starts
            self.mqtt_handler.publish_relay_state(i, False)
            self.mqtt_handler.publish_schedule_enabled(i, sched["schedule_enabled"])
            self.mqtt_handler.publish_start_times(i, sched["start_times"])
            self.mqtt_handler.publish_duration(i, sched["duration"])

    def run(self):
        self.running = True

        self.gpio_mgr = GPIOManager(config.RELAY_PINS, config.ACTIVE_LOW)

        self.scheduler = GardenScheduler(
            self.schedules, self.toggle_relay_from_scheduler
        )
        self.scheduler.start()

        if config.DHT_ENABLED:
            self.dht_sensor = DHTSensorManager(config.DHT_PIN)

        self.mqtt_handler = MQTTHandler(
            on_relay_toggle=self.on_relay_toggle,
            on_schedule_toggle=self.on_schedule_toggle,
            on_start_times_change=self.on_start_times_change,
            on_duration_change=self.on_duration_change,
        )
        self.mqtt_handler.connect()

        try:
            time.sleep(2.0)
            self.publish_initial_states()

            logger.info("Relay Controller Daemon is running. Press Ctrl+C to exit.")
            last_heartbeat_time = 0.0
            while self.running:
                now = time.time()

                if now - last_heartbeat_time >= config.HEARTBEAT_INTERVAL:
                    self.mqtt_handler.publish_heartbeat()
                    last_heartbeat_time = now

                if now - self.last_dht_read_time >= config.DHT_INTERVAL:
                    self.read_and_publish_dht()
                    self.last_dht_read_time = now

                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received, stopping...")
        finally:
            self.shutdown()

    def read_and_publish_dht(self):
        """Reads temperature and humidity from the DHT22 sensor and publishes to Home Assistant."""
        if self.dht_sensor:
            logger.info("Reading DHT22 sensor data...")
            temp, hum = self.dht_sensor.read()
            if temp is not None or hum is not None:
                self.mqtt_handler.publish_sensor_data(temp, hum)
            else:
                logger.warning("Failed to read data from DHT22 sensor")

    def shutdown(self):
        logger.info("Shutting down cleanly...")
        self.running = False

        if self.scheduler:
            self.scheduler.stop()

        if self.mqtt_handler:
            self.mqtt_handler.disconnect()

        if self.gpio_mgr:
            logger.info("Turning off all relays for safety.")
            for i in range(1, self.num_relays + 1):
                try:
                    self.gpio_mgr.turn_off(i)
                except Exception:
                    pass
            self.gpio_mgr.cleanup()

        logger.info("Shutdown complete.")


def main():
    app = GardenControllerApp()

    def signal_handler(signum, frame):
        logger.info(f"Received system signal {signum}")
        app.running = False

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    app.run()


if __name__ == "__main__":
    main()
