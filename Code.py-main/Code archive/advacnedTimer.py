import time

# How long we want the LED to stay on
BLINK_ON_DURATION = 0.5

# How long we want the LED to stay off
BLINK_OFF_DURATION = 0.25

while True:
    now = time.monotonic()
    print("hsould say zero",time.CLOCK_MONOTONIC)
    
    print(now)
    print("hey")
    time.sleep(1)
    print("2secods?",now)
    



