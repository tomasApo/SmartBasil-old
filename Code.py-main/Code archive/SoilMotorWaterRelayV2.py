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

timeOnHours = 8
timeOffHours = 22

soilBoundry = 822

def soil():
    touch = ss.moisture_read()
    if touch < soilBoundry:
        pinMotor.value = True
        print("motor should run", pinMotor.value)
        time.sleep(2)
    print(pinMotor.value)
    temp = ss.get_temp()

    pinMotor.value = False
    print("temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)


delta = (timeOffHours-timeOnHours)*60*60
remainer = (24*60*60) - delta

while True:
    pinRelay.value = False #Lights ON

    soil()      #Check soil
    soil()      #Check soil
    print("Time left before relay switches " +str(delta/(60*60)) + "h")
    time.sleep(delta)
    print(delta)
    soil()      #Check soil
    soil()      #Check soil

    #pinRelay.value = True  #Lights OFF

    time.sleep(remainer)   #insure that loop is exactly 24h


