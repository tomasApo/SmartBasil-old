import digitalio
 from adafruit_seesaw.seesaw import Seesaw
 import time

 i2c_bus = board.I2C()
 ss = Seesaw(i2c_bus, addr=0x36)


 pinMotor = digitalio.DigitalInOut(board.D19)
 @@ -13,46 +17,65 @@
 pinRelay = digitalio.DigitalInOut(board.D5)
 pinRelay.direction = digitalio.Direction.OUTPUT

 timeOnHours = 8
 timeOffHours = 22

 soilBoundry = 600

 def soil():
     touch = ss.moisture_read()
     if touch < soilBoundry:
         pinMotor.value = True
         print("motor should run", pinMotor.value)
         time.sleep(2)
     print("motor value:",pinMotor.value)
     temp = ss.get_temp()

     pinMotor.value = False
     print("temp: " + str(temp) + "  moisture: " + str(touch))
     time.sleep(1)


 delta = (timeOffHours-timeOnHours)*60*60
 remainer = (24*60*60) - delta

 while True:
     now = time.monotonic()
     print("Current time " + str(round((now/3600))) + "h")
     time.sleep(100)
     soil()
     time.sleep(100)
     soil()
     time.sleep(2)
     if now > (timeOffHours*60*60) or (now < (timeOnHours*60*60)):
         pinRelay.value = True  #Lights OFF
     if (now > (timeOnHours*60*60)) and (now > (timeOffHours*60*60)):
         pinRelay.value = False #Lights ON
     if now > 86400: #24h reset
        now=0
