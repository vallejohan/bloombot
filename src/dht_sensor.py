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
        self.last_valid_temp = None
        self.last_valid_hum = None

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
            logger.warning(
                "Linux Kernel IIO driver not found. Falling back to simulated/MOCK DHT22."
            )
            self.is_mock = True

    def read(self):
        """Reads temperature and humidity. Returns (temperature, humidity) tuple or (None, None) on failure."""
        if self.is_mock:
            temp = round(random.uniform(19.0, 23.0), 1)  # nosec B311
            humidity = round(random.uniform(50.0, 60.0), 1)  # nosec B311
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

                    temp_c = round(temp, 1)
                    humidity_pct = round(humidity, 1)

                    if not (-40.0 <= temp_c <= 80.0 and 0.0 <= humidity_pct <= 100.0):
                        logger.warning(
                            f"Discarding out-of-bounds sensor reading (attempt {attempt}/3): temp={temp_c}°C, hum={humidity_pct}%"
                        )
                        if attempt < 3:
                            time.sleep(1.0)
                        continue

                    if self.last_valid_temp is not None:
                        if abs(temp_c - self.last_valid_temp) > 10.0:
                            logger.warning(
                                f"Discarding temperature spike (attempt {attempt}/3): {temp_c}°C (previous: {self.last_valid_temp}°C)"
                            )
                            if attempt < 3:
                                time.sleep(1.0)
                            continue

                    if self.last_valid_hum is not None:
                        if abs(humidity_pct - self.last_valid_hum) > 30.0:
                            logger.warning(
                                f"Discarding humidity spike (attempt {attempt}/3): {humidity_pct}% (previous: {self.last_valid_hum}%)"
                            )
                            if attempt < 3:
                                time.sleep(1.0)
                            continue

                    self.last_valid_temp = temp_c
                    self.last_valid_hum = humidity_pct
                    return temp_c, humidity_pct
                except Exception as e:
                    logger.warning(
                        f"Error reading from Linux Kernel IIO driver (attempt {attempt}/3): {e}"
                    )
                    if attempt < 3:
                        time.sleep(1.0)
            return None, None
