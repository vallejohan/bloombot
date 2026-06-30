import logging

logger = logging.getLogger(__name__)


class MockOutputDevice:
    """Mock implementation of a GPIO output pin for testing on non-Pi platforms."""

    def __init__(self, pin, active_high=True, initial_value=False):
        self.pin = pin
        self.active_high = active_high
        self._value = initial_value
        logger.info(
            f"[GPIO-MOCK] Initialized pin BCM {pin} (active_high={active_high}, initial_value={initial_value})"
        )

    @property
    def value(self):
        return self._value

    def on(self):
        self._value = True
        logger.info(
            f"[GPIO-MOCK] Pin BCM {self.pin} -> ON (Physical output: {'LOW' if not self.active_high else 'HIGH'})"
        )

    def off(self):
        self._value = False
        logger.info(
            f"[GPIO-MOCK] Pin BCM {self.pin} -> OFF (Physical output: {'HIGH' if not self.active_high else 'LOW'})"
        )


class GPIOManager:
    """Manages physical and mock GPIO output devices for the relays."""

    def __init__(self, pins, active_low=True):
        self.pins = pins
        self.active_low = active_low
        self.devices = {}
        self.is_mock = False
        active_high = not active_low

        try:
            from gpiozero import OutputDevice

            logger.info("Using 'gpiozero' library for GPIO control.")
            for i, pin in enumerate(pins):
                # active_high=False in gpiozero means active-low (ON pulls pin LOW)
                self.devices[i + 1] = OutputDevice(
                    pin=pin, active_high=active_high, initial_value=False
                )
            return
        except (ImportError, RuntimeError) as e:
            logger.warning(f"Could not load gpiozero: {e}. Falling back to MOCK GPIO.")

        self.is_mock = True
        for i, pin in enumerate(pins):
            self.devices[i + 1] = MockOutputDevice(
                pin=pin, active_high=active_high, initial_value=False
            )

    def turn_on(self, relay_num):
        """Turn on the specified relay (1-based index)."""
        if relay_num in self.devices:
            self.devices[relay_num].on()
            logger.info(f"Relay {relay_num} turned ON")
        else:
            logger.error(f"Invalid relay number: {relay_num}")

    def turn_off(self, relay_num):
        """Turn off the specified relay (1-based index)."""
        if relay_num in self.devices:
            self.devices[relay_num].off()
            logger.info(f"Relay {relay_num} turned OFF")
        else:
            logger.error(f"Invalid relay number: {relay_num}")

    def get_state(self, relay_num):
        """Get the current ON/OFF state of the specified relay (1-based index)."""
        if relay_num in self.devices:
            return self.devices[relay_num].value
        return False

    def cleanup(self):
        """Clean up GPIO resources."""
        logger.info("Cleaning up GPIO resources.")
        if self.is_mock:
            return

        # If we used gpiozero, devices will automatically close when garbage collected or script exits
        for dev in self.devices.values():
            try:
                dev.close()
            except AttributeError:
                pass
