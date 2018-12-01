import time
import socket
from machine import Pin, Timer
from network import LoRa

lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

echo1 = Pin('G22', mode=Pin.IN)
trigger1 = Pin('G17', mode=Pin.OUT)

echo2 = Pin('G16', mode=Pin.IN)
trigger2 = Pin('G15', mode=Pin.OUT)

echo3 = Pin('G14', mode=Pin.IN)
trigger3 = Pin('G13', mode=Pin.OUT)

p_blue_light = Pin('G23', mode=Pin.OUT)
p_red_light = Pin('G24', mode=Pin.OUT)
p_green_light = Pin('G11', mode=Pin.OUT)

'''
b_pin = Pin('G22', mode=Pin.OUT)
a_pin = Pin('G17', mode=Pin.OUT)
f_pin = Pin('G16', mode=Pin.OUT)
g_pin = Pin('G15', mode=Pin.OUT)
e_pin = Pin('G14', mode=Pin.OUT)
d_pin = Pin('G13', mode=Pin.OUT)
c_pin = Pin('G12', mode=Pin.OUT)
'''
#------------------------------ Network ---------------


def networking(count):

    s.setblocking(True)
    s.send(str(count).encode("hex"))
    #s.send("Ping".encode("hex"))
    print("Sending free lot number :", count)
    s.setblocking(False)
    #if s.recv(64) == b"Pong":
    #    print("Ack")
    # print('Ping-' + str(count))
    # count += 1
    time.sleep(1)

#------------------------------------------------------------

chrono = Timer.Chrono()

trigger1(0)
trigger2(0)
trigger3(0)

#----------------------------------- Sensor 1 ------------------------

while True:
    count = 3
    chrono.reset()

    trigger1(1)
    time.sleep_us(10)
    trigger1(0)

    while echo1() == 0:
        pass

    chrono.start()

    while echo1() == 1:
        pass

    chrono.stop()

    distance1 = chrono.read_us() / 58.0

    if distance1 <= 7:
        p_green_light.value(1)
        count -= 1
    else:
        p_green_light.value(0)

    if distance1 > 400:
        print("Out of range")
    else:
        print("Sensor 1 {:.0f} cm".format(distance1))
    
    time.sleep(0.1)

    #-------------------- Sensor 2 -----------------------------------

    chrono.reset()

    trigger2(1)
    time.sleep_us(10)
    trigger2(0)

    while echo2() == 0:
        pass

    chrono.start()

    while echo2() == 1:
        pass

    chrono.stop()

    distance2 = chrono.read_us() / 58.0

    if distance2 <= 7:
        p_red_light.value(1)
        count -= 1
    else:
        p_red_light.value(0)

    if distance2 > 400:
        print("Out of range")
    else:
        print("Sensor 2 {:.0f} cm".format(distance2))
    
    time.sleep(0.1)

#----------------------------- Sensor 3 --------------------------------

    chrono.reset()

    trigger3(1)
    time.sleep_us(10)
    trigger3(0)

    while echo3() == 0:
        pass

    chrono.start()

    while echo3() == 1:
        pass

    chrono.stop()

    distance3 = chrono.read_us() / 58.0

    if distance3 <= 7:
        p_blue_light.value(1)
        count -= 1
    else:
        p_blue_light.value(0)

    if distance3 > 400:
        print("Out of range")
    else:
        print("Sensor 3 {:.0f} cm".format(distance3))
    
    time.sleep(0.1)
    networking(count)


