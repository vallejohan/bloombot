import json
import os
import sys
import unittest
from unittest.mock import MagicMock, mock_open, patch

# Add src/ directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import main


class TestGardenControllerApp(unittest.TestCase):
    @patch("main.os.path.exists", return_value=False)
    @patch("main.open", new_callable=mock_open)
    def setUp(self, mock_file, mock_exists):
        self.app = main.GardenControllerApp()
        self.app.gpio_mgr = MagicMock()
        self.app.mqtt_handler = MagicMock()
        self.app.scheduler = MagicMock()
        self.app.dht_sensor = MagicMock()

    @patch("main.open", new_callable=mock_open)
    def test_load_schedules_default_creation(self, mock_file):
        """Test that missing schedule files initialize default configurations for all relays dynamically."""
        self.assertEqual(len(self.app.schedules), self.app.num_relays)
        for i in range(1, self.app.num_relays + 1):
            key = f"relay_{i}"
            self.assertIn(key, self.app.schedules)
            self.assertFalse(self.app.schedules[key]["schedule_enabled"])
            self.assertEqual(len(self.app.schedules[key]["start_times"]), 1)
            self.assertEqual(
                self.app.schedules[key]["start_times"][0]["time"], "08:00:00"
            )
            self.assertTrue(self.app.schedules[key]["start_times"][0]["enabled"])
            self.assertEqual(self.app.schedules[key]["duration"], 10)

    @patch("main.open", new_callable=mock_open)
    def test_on_relay_toggle_on(self, mock_file):
        """Test that receiving an ON manual override toggles the physical/mock GPIO pin and publishes the state back to HA."""
        for i in range(1, self.app.num_relays + 1):
            self.app.gpio_mgr.turn_on.reset_mock()
            self.app.mqtt_handler.publish_relay_state.reset_mock()

            self.app.on_relay_toggle(i, True)

            self.app.gpio_mgr.turn_on.assert_called_once_with(i)
            self.app.mqtt_handler.publish_relay_state.assert_called_once_with(i, True)

    @patch("main.open", new_callable=mock_open)
    def test_on_relay_toggle_off(self, mock_file):
        """Test that receiving an OFF manual override toggles the physical/mock GPIO pin, cancels scheduler run timers, and updates HA."""
        for i in range(1, self.app.num_relays + 1):
            self.app.gpio_mgr.turn_off.reset_mock()
            self.app.scheduler.cancel_active_run.reset_mock()
            self.app.mqtt_handler.publish_relay_state.reset_mock()

            self.app.on_relay_toggle(i, False)

            self.app.gpio_mgr.turn_off.assert_called_once_with(i)
            self.app.scheduler.cancel_active_run.assert_called_once_with(i)
            self.app.mqtt_handler.publish_relay_state.assert_called_once_with(i, False)

    @patch("main.open", new_callable=mock_open)
    def test_on_schedule_toggle(self, mock_file):
        """Test that toggling a schedule's active state updates internal configurations, triggers saves, and publishes status back to HA."""
        for i in range(1, self.app.num_relays + 1):
            self.app.mqtt_handler.publish_schedule_enabled.reset_mock()

            # Enable schedule
            self.app.on_schedule_toggle(i, True)
            self.assertTrue(self.app.schedules[f"relay_{i}"]["schedule_enabled"])
            self.app.mqtt_handler.publish_schedule_enabled.assert_called_once_with(
                i, True
            )

            # Disable schedule
            self.app.on_schedule_toggle(i, False)
            self.assertFalse(self.app.schedules[f"relay_{i}"]["schedule_enabled"])
            self.app.mqtt_handler.publish_schedule_enabled.assert_called_with(i, False)

    @patch("main.open", new_callable=mock_open)
    def test_on_start_times_change_valid(self, mock_file):
        """Test that schedule start times changes with valid payloads are saved and published."""
        valid_payload = json.dumps(
            [{"time": "14:15", "enabled": True}, {"time": "22:30:15", "enabled": False}]
        )
        for i in range(1, self.app.num_relays + 1):
            self.app.mqtt_handler.publish_start_times.reset_mock()

            self.app.on_start_times_change(i, valid_payload)
            expected = [
                {"time": "14:15:00", "enabled": True},
                {"time": "22:30:15", "enabled": False},
            ]
            self.assertEqual(self.app.schedules[f"relay_{i}"]["start_times"], expected)
            self.app.mqtt_handler.publish_start_times.assert_called_once_with(
                i, expected
            )

    @patch("main.open", new_callable=mock_open)
    def test_on_start_times_change_invalid(self, mock_file):
        """Test that schedule start times changes with invalid payloads preserve previous state."""
        for i in range(1, self.app.num_relays + 1):
            initial_state = [{"time": "08:00:00", "enabled": True}]
            self.app.schedules[f"relay_{i}"]["start_times"] = initial_state
            self.app.mqtt_handler.publish_start_times.reset_mock()

            # Empty list (invalid since at least one is required)
            self.app.on_start_times_change(i, json.dumps([]))
            self.assertEqual(
                self.app.schedules[f"relay_{i}"]["start_times"], initial_state
            )

            # Not a list
            self.app.on_start_times_change(i, json.dumps({"time": "12:00:00"}))
            self.assertEqual(
                self.app.schedules[f"relay_{i}"]["start_times"], initial_state
            )

            # Invalid time format
            invalid_payload = json.dumps([{"time": "25:00", "enabled": True}])
            self.app.on_start_times_change(i, invalid_payload)
            self.assertEqual(
                self.app.schedules[f"relay_{i}"]["start_times"], initial_state
            )

    @patch("main.open", new_callable=mock_open)
    def test_on_duration_change(self, mock_file):
        """Test that watering duration adjustments are constrained to valid limits (1-180 min), saved, and synchronized to HA."""
        for i in range(1, self.app.num_relays + 1):
            self.app.mqtt_handler.publish_duration.reset_mock()

            self.app.on_duration_change(i, 5)
            self.assertEqual(self.app.schedules[f"relay_{i}"]["duration"], 5)
            self.app.mqtt_handler.publish_duration.assert_called_once_with(i, 5)

            # Testing boundary constraints (1 to 10 mins)
            self.app.on_duration_change(i, 0)
            self.assertEqual(self.app.schedules[f"relay_{i}"]["duration"], 1)

            self.app.on_duration_change(i, 20)
            self.assertEqual(self.app.schedules[f"relay_{i}"]["duration"], 10)

    @patch("main.open", new_callable=mock_open)
    def test_toggle_relay_from_scheduler(self, mock_file):
        """Test that scheduled controller trigger actions switch the physical/mock GPIO pins and publish states to HA."""
        for i in range(1, self.app.num_relays + 1):
            self.app.gpio_mgr.turn_on.reset_mock()
            self.app.mqtt_handler.publish_relay_state.reset_mock()

            self.app.toggle_relay_from_scheduler(i, True)
            self.app.gpio_mgr.turn_on.assert_called_once_with(i)
            self.app.mqtt_handler.publish_relay_state.assert_called_once_with(i, True)

    @patch("main.open", new_callable=mock_open)
    def test_publish_initial_states(self, mock_file):
        """Test that initial synchronization publishes start states for all active relays to Home Assistant correctly."""
        self.app.publish_initial_states()
        self.assertEqual(
            self.app.mqtt_handler.publish_relay_state.call_count, self.app.num_relays
        )
        self.assertEqual(
            self.app.mqtt_handler.publish_schedule_enabled.call_count,
            self.app.num_relays,
        )
        self.assertEqual(
            self.app.mqtt_handler.publish_start_times.call_count, self.app.num_relays
        )
        self.assertEqual(
            self.app.mqtt_handler.publish_duration.call_count, self.app.num_relays
        )

    def test_read_and_publish_dht_success(self):
        """Test that read_and_publish_dht reads from sensor and publishes to MQTT."""
        self.app.dht_sensor = MagicMock()
        self.app.dht_sensor.read.return_value = (22.5, 55.2)

        self.app.read_and_publish_dht()

        self.app.dht_sensor.read.assert_called_once()
        self.app.mqtt_handler.publish_sensor_data.assert_called_once_with(22.5, 55.2)

    def test_read_and_publish_dht_failure(self):
        """Test that read_and_publish_dht handles None return values from sensor gracefully."""
        self.app.dht_sensor = MagicMock()
        self.app.dht_sensor.read.return_value = (None, None)

        self.app.read_and_publish_dht()

        self.app.dht_sensor.read.assert_called_once()
        self.app.mqtt_handler.publish_sensor_data.assert_not_called()

    def test_read_and_publish_dht_no_sensor(self):
        """Test that read_and_publish_dht does nothing if sensor is not initialized."""
        self.app.dht_sensor = None

        self.app.read_and_publish_dht()

        self.app.mqtt_handler.publish_sensor_data.assert_not_called()


if __name__ == "__main__":
    unittest.main()
