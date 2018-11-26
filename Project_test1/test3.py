import time
from machine import Pin, Timer

echo = Pin(Pin.exp_board.G7, mode=Pin.IN)
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT)
p_light = Pin('G10', mode=Pin.OUT)

trigger(0)

chrono = Timer.Chrono()

while True:
    chrono.reset()

    trigger(1)
    time.sleep_us(10)
    trigger(0)

    while echo() == 0:
        pass

    chrono.start()

    while echo() == 1:
        pass

    chrono.stop()

    distance = chrono.read_us() / 58.0
    if distance <= 7:
        p_light.value(1)
    else:
        p_light.value(0)

    if distance > 400:
        print("Out of range")
    else:
        print("Distance {:.0f} cm".format(distance))
        

    time.sleep(1)