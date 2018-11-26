from machine import Pin
import time
import utime
import machine
from machine import Timer

start = 0
end = 0

p_light = Pin('P20', mode=Pin.OUT)
p_light.value(1)

p_trig = Pin("G30", mode=Pin.OUT) # Trig = 30
p_echo = Pin("G31", mode=Pin.IN) # Echo = 31

chrono = Timer.Chrono()
chrono.reset()

p_trig.value(1)
Timer.sleep_us(10)
p_trig.value(0)

while(p_echo.value() == 0):
    start = chrono.read_us()
    print(start)

while(p_echo.value() == 1):
    end = chrono.read_us()
    print(end)

chrono.stop()

print(start, end)

'''
while(True):
    p_tring.value(1)
    time.sleep(.10) #sec
    p_tring.value(0)

    pulse_width = pulseIn(p_echo, 1)

    print(pulse_width)

    print("Pulse Width: %d" %pulse_width)
    
    distance = (pulse_width/29)/2

    print("Distance: %d" %distance)

    time.sleep(1)
'''

