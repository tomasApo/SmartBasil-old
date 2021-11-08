import board
import digitalio
from adafruit_seesaw.seesaw import Seesaw
import time

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

pinMotor = digitalio.DigitalInOut(board.D19)
pinMotor.direction = digitalio.Direction.OUTPUT

pinRelay = digitalio.DigitalInOut(board.D5)
pinRelay.direction = digitalio.Direction.OUTPUT

# -----------------------------------------------
timeOnHours = 8
timeOffHours = 22
soilBoundry = 600
# -----------------------------------------------

def soil():
    mList = []  # Uses a list with a while loop to find the mean called touchmean
    i = 0
    while i < 5:
        mList.append(ss.moisture_read())
        time.sleep(1)
        i = i + 1
    touchMean = (sum(mList))/(len(mList))
    
    if touchMean < soilBoundry:  # This is for the pump + soil sensor
        pinMotor.value = True
        print("Motor should run", pinMotor.value)
        time.sleep(10)

    temp = ss.get_temp()

    pinMotor.value = False
    print("Temp:" + str(temp) + "  Moisture:" + str(touchMean))
    time.sleep(1)


while True:
    now = time.monotonic()
    print("Current time " + str(round((now/3600), 2)) + "h")
    time.sleep(1)
    soil()
    time.sleep(1)
    if now > 86400:  # 24h reset
        now = 0
    if (now > (timeOffHours*60*60)) or (now < (timeOnHours*60*60)):
        pinRelay.value = True  # Lights OFF
        print("1")
    if (now > (timeOnHours*60*60)) and (now < (timeOffHours*60*60)):
        pinRelay.value = False  # Lights ON
        print("2")
    
    print("relay status", pinRelay.value)
    time.sleep(60)




