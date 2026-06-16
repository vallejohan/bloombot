import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Add src/ directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import gpio_manager


class TestGPIOManager(unittest.TestCase):
    @patch("gpio_manager.logger")
    def test_gpio_manager_mock_fallback(self, mock_logger):
        """Test that GPIOManager falls back to Mock mode when physical libraries are not present, and that states change correctly."""
        # Force import errors for physical libraries to ensure mock fallback
        with patch.dict("sys.modules", {"gpiozero": None, "RPi.GPIO": None}):
            mgr = gpio_manager.GPIOManager([5, 6, 13], active_low=True)
            self.assertTrue(mgr.is_mock)
            self.assertEqual(len(mgr.devices), 3)

            # Check that initial state is OFF (value is False)
            self.assertFalse(mgr.get_state(1))

            # Turn ON first relay and verify state
            mgr.turn_on(1)
            self.assertTrue(mgr.get_state(1))
            self.assertFalse(mgr.get_state(2))

            # Turn OFF first relay and verify state
            mgr.turn_off(1)
            self.assertFalse(mgr.get_state(1))

    @patch("gpio_manager.logger")
    def test_gpio_manager_invalid_relay(self, mock_logger):
        """Test that operations on non-existent relay numbers are gracefully handled (log error rather than crash)."""
        with patch.dict("sys.modules", {"gpiozero": None, "RPi.GPIO": None}):
            mgr = gpio_manager.GPIOManager([5, 6], active_low=True)

            # Non-existent relay operations (should log error and not crash)
            mgr.turn_on(3)
            mock_logger.error.assert_called_with("Invalid relay number: 3")

            mgr.turn_off(3)
            mock_logger.error.assert_called_with("Invalid relay number: 3")

            self.assertFalse(mgr.get_state(3))


if __name__ == "__main__":
    unittest.main()
