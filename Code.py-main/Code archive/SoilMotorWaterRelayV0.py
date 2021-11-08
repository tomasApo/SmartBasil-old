# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board
import digitalio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()

ss = Seesaw(i2c_bus, addr=0x36)

pinMotor = digitalio.DigitalInOut(board.D6)
pinMotor.direction = digitalio.Direction.OUTPUT

pinRelay = digitalio.DigitalInOut(board.D5)
pinRelay.direction = digitalio.Direction.OUTPUT

time = 0
#8:00 on 0
#22:00 off
#dif 3600s
    print("penis")
    time.sleep(5)
while True:
    if time>3600s
    pinRelay.value = True
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    if touch < 822:
        #pinMotor.value = True
        print("motor should run", pinMotor.value)
        #D21
        time.sleep(2)
    print(pinMotor.value)
    temp = ss.get_temp()
    # read temperature from the temperature sensor

    pinMotor.value = True
    print("temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)


