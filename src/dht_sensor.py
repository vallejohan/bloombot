import glob
import logging
import os
import random
import time

logger = logging.getLogger(__name__)


class DHTSensorManager:
    """Manages reading from a physical DHT22 sensor via the Linux kernel IIO driver, falling back to mock values."""

    def __init__(self, pin: int):
        self.pin = pin
        self.is_mock = False
        self.iio_path = None

        try:
            iio_devices = glob.glob("/sys/bus/iio/devices/iio:device*")
            for dev_path in iio_devices:
                temp_file = os.path.join(dev_path, "in_temp_input")
                hum_file = os.path.join(dev_path, "in_humidityrelative_input")
                if os.path.exists(temp_file) and os.path.exists(hum_file):
                    self.iio_path = dev_path
                    logger.info(f"Using Linux Kernel IIO driver at {self.iio_path}")
                    break
        except Exception as e:
            logger.debug(f"Failed to search for kernel IIO driver paths: {e}")
        
        if not self.iio_path:
            logger.warning("Linux Kernel IIO driver not found. Falling back to simulated/MOCK DHT22.")
            self.is_mock = True

    def read(self):
        """Reads temperature and humidity. Returns (temperature, humidity) tuple or (None, None) on failure."""
        if self.is_mock:
            # Generate realistic fluctuating weather data:
            temp = round(random.uniform(19.0, 23.0), 1)
            humidity = round(random.uniform(50.0, 60.0), 1)
            logger.debug(f"[DHT-MOCK] Read temperature={temp}°C, humidity={humidity}%")
            return temp, humidity

        # Read via Linux Kernel IIO Driver
        if self.iio_path:
            for attempt in range(1, 4):
                try:
                    temp_file = os.path.join(self.iio_path, "in_temp_input")
                    hum_file = os.path.join(self.iio_path, "in_humidityrelative_input")

                    with open(temp_file, "r") as f:
                        temp = float(f.read().strip()) / 1000.0
                    with open(hum_file, "r") as f:
                        humidity = float(f.read().strip()) / 1000.0

                    return round(temp, 1), round(humidity, 1)
                except Exception as e:
                    logger.warning(
                        f"Error reading from Linux Kernel IIO driver (attempt {attempt}/3): {e}"
                    )
                    if attempt < 3:
                        time.sleep(1.0)
            return None, None

    def cleanup(self):
        """Releases sensor hardware resources (no-op for kernel driver)."""
        pass
