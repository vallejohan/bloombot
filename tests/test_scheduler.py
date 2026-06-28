import os
import sys
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

# Add src/ directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import scheduler


class TestGardenScheduler(unittest.TestCase):
    def test_init(self):
        """Test that the scheduler initializes with the correct schedules, callbacks, and default empty states."""
        schedules = {"relay_1": {"schedule_enabled": True}}
        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)

        self.assertEqual(sched.schedules, schedules)
        self.assertEqual(sched.toggle_relay_callback, callback)
        self.assertEqual(sched.active_runs, {})
        self.assertFalse(sched._running)

    def test_cancel_active_run(self):
        """Test that cancelling an active run removes the relay's record from active_runs."""
        schedules = {}
        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched.active_runs[1] = 123456789.0

        # Cancel non-existent run (should not raise error)
        sched.cancel_active_run(2)
        self.assertEqual(len(sched.active_runs), 1)

        # Cancel active run
        sched.cancel_active_run(1)
        self.assertNotIn(1, sched.active_runs)

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_triggers_schedule_1_hms(self, mock_datetime, mock_time, mock_sleep):
        """Test that the scheduler loop triggers scheduled watering when the system time matches a HH:MM:SS format start_times time."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "08:00:00",
            "%H:%M": "08:00",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now

        mock_time.return_value = 1000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {
            "relay_1": {
                "schedule_enabled": True,
                "start_times": [
                    {"time": "08:00:00", "enabled": True}
                ],
                "duration": 5,
            }
        }

        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched._running = True
        sched._run_loop()

        callback.assert_called_once_with(1, True, is_scheduled=True)
        self.assertEqual(sched.active_runs[1], 1000.0 + (5 * 60))

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_triggers_schedule_2_hms(self, mock_datetime, mock_time, mock_sleep):
        """Test that the scheduler loop triggers scheduled watering for secondary time when enabled."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "20:00:00",
            "%H:%M": "20:00",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now

        mock_time.return_value = 1000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {
            "relay_1": {
                "schedule_enabled": True,
                "start_times": [
                    {"time": "08:00:00", "enabled": False},
                    {"time": "20:00:00", "enabled": True}
                ],
                "duration": 5,
            }
        }

        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched._running = True
        sched._run_loop()

        callback.assert_called_once_with(1, True, is_scheduled=True)
        self.assertEqual(sched.active_runs[1], 1000.0 + (5 * 60))

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_triggers_schedule_hm(self, mock_datetime, mock_time, mock_sleep):
        """Test that the scheduler loop triggers scheduled watering when the system time matches a HH:MM format time."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "08:00:00",
            "%H:%M": "08:00",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now

        mock_time.return_value = 1000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {
            "relay_2": {
                "schedule_enabled": True,
                "start_times": [
                    {"time": "08:00", "enabled": True}
                ],
                "duration": 10
            }
        }

        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched._running = True
        sched._run_loop()

        callback.assert_called_once_with(2, True, is_scheduled=True)
        self.assertEqual(sched.active_runs[2], 1000.0 + (10 * 60))

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_does_not_trigger_when_disabled(
        self, mock_datetime, mock_time, mock_sleep
    ):
        """Test that the scheduler loop does not trigger watering when schedule_enabled is set to False."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "08:00:00",
            "%H:%M": "08:00",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now
        mock_time.return_value = 1000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {
            "relay_1": {
                "schedule_enabled": False,
                "start_times": [
                    {"time": "08:00:00", "enabled": True}
                ],
                "duration": 5,
            }
        }

        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched._running = True
        sched._run_loop()

        callback.assert_not_called()
        self.assertEqual(sched.active_runs, {})

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_does_not_trigger_when_start_time_disabled(
        self, mock_datetime, mock_time, mock_sleep
    ):
        """Test that the scheduler loop does not trigger watering when all start times are disabled."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "08:00:00",
            "%H:%M": "08:00",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now
        mock_time.return_value = 1000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {
            "relay_1": {
                "schedule_enabled": True,
                "start_times": [
                    {"time": "08:00:00", "enabled": False}
                ],
                "duration": 5,
            }
        }

        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched._running = True
        sched._run_loop()

        callback.assert_not_called()
        self.assertEqual(sched.active_runs, {})

    @patch("scheduler.time.sleep")
    @patch("scheduler.time.time")
    @patch("scheduler.datetime")
    def test_run_loop_expires_duration(self, mock_datetime, mock_time, mock_sleep):
        """Test that the scheduler loop automatically turns off relays when their active watering duration has elapsed."""
        mock_now = MagicMock()
        mock_now.strftime.side_effect = lambda fmt: {
            "%H:%M:%S": "08:15:00",
            "%H:%M": "08:15",
        }[fmt]
        mock_now.second = 0
        mock_datetime.now.return_value = mock_now

        # Set epoch time past the end time of the active run
        mock_time.return_value = 2000.0

        def stop_loop(*args):
            sched._running = False

        mock_sleep.side_effect = stop_loop

        schedules = {}
        callback = MagicMock()
        sched = scheduler.GardenScheduler(schedules, callback)
        sched.active_runs[3] = 1800.0  # Ended at 1800.0
        sched._running = True
        sched._run_loop()

        callback.assert_called_once_with(3, False, is_scheduled=True)
        self.assertNotIn(3, sched.active_runs)


if __name__ == "__main__":
    unittest.main()
