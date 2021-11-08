import board
import digitalio
from adafruit_seesaw.seesaw import Seesaw
import time
import busio
import adafruit_pcf8523


myI2C = busio.I2C(board.SCL, board.SDA)

rtc = adafruit_pcf8523.PCF8523(myI2C)
ss = Seesaw(myI2C, addr=0x36)


pinMotor = digitalio.DigitalInOut(board.D19)
pinMotor.direction = digitalio.Direction.OUTPUT

pinRelay = digitalio.DigitalInOut(board.D5)
pinRelay.direction = digitalio.Direction.OUTPUT

# -----------------------------------------------
timeOnHours = 8
timeOffHours = 22
soilBoundry = 600
# -----------------------------------------------

if True:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2021,  10,   22,   21,  59,  15,    0,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    rtc.datetime = t
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


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
    t = rtc.datetime
    print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mday, t.tm_mon, t.tm_year))
    print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))

    time.sleep(1)

    now=t.tm_hour

    print("Current time ", now)
    time.sleep(1)
    soil()
    time.sleep(1)
    if (now > timeOffHours) or (now < timeOnHours):
        pinRelay.value = True  # Lights OFF
        print("1")
    elif (now > timeOnHours) and (now < timeOffHours):
        pinRelay.value = False  # Lights ON
        print("2")

    print("relay status", pinRelay.value)
    time.sleep(2)




