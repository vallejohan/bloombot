import logging
import threading
import time
from datetime import datetime

import config

logger = logging.getLogger(__name__)


class GardenScheduler:
    """Manages background checking of relay schedules and watering durations."""

    def __init__(self, schedules, toggle_relay_callback):
        self.schedules = schedules  # Shared schedules dict
        self.toggle_relay_callback = toggle_relay_callback

        # Tracks active schedule runs: {relay_num: end_epoch_timestamp}
        self.active_runs = {}

        # Thread control
        self._running = False
        self._thread = None
        self._lock = threading.Lock()

    def start(self):
        """Start the scheduler background thread."""
        logger.info("Starting scheduler thread...")
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, name="SchedulerThread")
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        """Stop the scheduler background thread."""
        logger.info("Stopping scheduler thread...")
        self._running = False
        if self._thread:
            self._thread.join(timeout=3.0)

    def cancel_active_run(self, relay_num):
        """Cancels an active scheduled run for a relay (e.g. if manually turned OFF)."""
        with self._lock:
            if relay_num in self.active_runs:
                logger.info(f"Cancelling active schedule timer for Relay {relay_num}")
                del self.active_runs[relay_num]

    def _run_loop(self):
        """Main scheduler loop running once per second."""
        while self._running:
            try:
                now = datetime.now()
                current_epoch = time.time()

                # Formats for comparison
                current_time_hms = now.strftime("%H:%M:%S")
                current_time_hm = now.strftime("%H:%M")

                with self._lock:
                    # 1. Check if any relay schedule should start
                    for relay_num in range(1, len(config.RELAY_PINS) + 1):
                        relay_key = f"relay_{relay_num}"
                        sched = self.schedules.get(relay_key, {})

                        if not sched.get("schedule_enabled", False):
                            continue

                        # Check all dynamic start times
                        start_times_list = sched.get(
                            "start_times", [{"time": "08:00:00", "enabled": True}]
                        )
                        times_to_check = [
                            item["time"]
                            for item in start_times_list
                            if item.get("enabled", False)
                        ]

                        for start_time in times_to_check:
                            # Match HH:MM:SS or HH:MM
                            is_match = False
                            if len(start_time) == 5:  # HH:MM
                                # Trigger at the 00th second of that minute
                                is_match = (
                                    current_time_hm == start_time and now.second == 0
                                )
                            else:  # HH:MM:SS
                                is_match = current_time_hms == start_time

                            if is_match:
                                # Verify if already watering under a schedule
                                if relay_num not in self.active_runs:
                                    duration_min = sched.get("duration", 10)
                                    duration_sec = duration_min * 60

                                    # Start scheduled watering
                                    logger.info(
                                        f"[SCHEDULER] Triggering schedule for Relay {relay_num} at {start_time} for {duration_min} minutes."
                                    )
                                    self.active_runs[relay_num] = (
                                        current_epoch + duration_sec
                                    )
                                    self.toggle_relay_callback(
                                        relay_num, True, is_scheduled=True
                                    )
                                    break

                    # 2. Check if any active scheduled watering should stop
                    expired_relays = []
                    for relay_num, end_time in self.active_runs.items():
                        if current_epoch >= end_time:
                            expired_relays.append(relay_num)

                    for relay_num in expired_relays:
                        logger.info(
                            f"[SCHEDULER] Duration expired for Relay {relay_num}. Shutting down."
                        )
                        del self.active_runs[relay_num]
                        self.toggle_relay_callback(relay_num, False, is_scheduled=True)

            except Exception as e:
                logger.error(f"Error in scheduler loop: {e}")

            time.sleep(1.0)
