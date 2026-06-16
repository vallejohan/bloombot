import logging
import random

logger = logging.getLogger(__name__)


class DHTSensorManager:
    """Manages reading from a physical DHT22 sensor, falling back to mock values on non-Pi platforms."""

    def __init__(self, pin: int):
        self.pin = pin
        self.sensor = None
        self.is_mock = False

        try:
            import adafruit_dht
            import board

            # Map pin number to board Pin object (e.g. 4 -> board.D4)
            pin_name = f"D{pin}"
            if hasattr(board, pin_name):
                board_pin = getattr(board, pin_name)
                self.sensor = adafruit_dht.DHT22(board_pin, use_pulseio=False)
                logger.info(
                    f"Using physical DHT22 sensor on BCM pin {pin} (board.{pin_name})"
                )
            else:
                raise ValueError(f"Pin '{pin_name}' not found on board module")
        except (ImportError, RuntimeError, ValueError, AttributeError) as e:
            logger.warning(
                f"Could not load physical DHT22 sensor library ({e}). Falling back to simulated/MOCK DHT22."
            )
            self.is_mock = True

    def read(self):
        """Reads temperature and humidity. Returns (temperature, humidity) tuple or (None, None) on failure."""
        if self.is_mock:
            # Generate realistic fluctuating weather data:
            # Temp: around 21°C +/- 2°C
            # Humidity: around 55% +/- 5%
            temp = round(random.uniform(19.0, 23.0), 1)
            humidity = round(random.uniform(50.0, 60.0), 1)
            logger.debug(f"[DHT-MOCK] Read temperature={temp}°C, humidity={humidity}%")
            return temp, humidity

        import time
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                # Read from adafruit_dht sensor
                temp = self.sensor.temperature
                humidity = self.sensor.humidity
                if temp is not None and humidity is not None:
                    return round(float(temp), 1), round(float(humidity), 1)
                else:
                    logger.warning(f"DHT22 returned empty reading (attempt {attempt}/{max_retries})")
            except Exception as e:
                logger.warning(
                    f"Error reading from physical DHT22 sensor (attempt {attempt}/{max_retries}): {e}"
                )
            
            if attempt < max_retries:
                time.sleep(2.0)
                
        return None, None

    def cleanup(self):
        """Releases physical sensor hardware resources."""
        if not self.is_mock and self.sensor is not None:
            logger.info("Cleaning up DHT22 sensor resources.")
            try:
                self.sensor.exit()
            except Exception as e:
                logger.error(f"Failed to exit DHT22 sensor: {e}")
