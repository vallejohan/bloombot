import time
from gpiozero import OutputDevice
from gpiozero.devices import device

print("=" * 50)
print(f"Active gpiozero Pin Factory: {device.pin_factory.__class__.__name__}")
print("=" * 50)

# Initialize BCM GPIO 5 as active-low (active_high=False)
try:
    print("Initializing BCM GPIO 5 (Physical Pin 29)...")
    relay = OutputDevice(5, active_high=False, initial_value=False)
    
    print("\nState: OFF (Inactive)")
    print("Physical voltage on BCM 5 should be: 3.3V")
    relay.off()
    time.sleep(5)
    
    print("\nState: ON (Active)")
    print("Physical voltage on BCM 5 should be: 0V")
    relay.on()
    time.sleep(5)
    
    print("\nState: OFF (Inactive)")
    print("Physical voltage on BCM 5 should be: 3.3V")
    relay.off()
    time.sleep(2)
    
    print("\nTest complete!")
except Exception as e:
    print(f"Error occurred: {e}")
