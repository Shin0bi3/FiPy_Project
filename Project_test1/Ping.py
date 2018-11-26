from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# count = 0
while True:
    s.sendall("Ping")
    print("Sending")
    if s.recv(64) == (b"Pong"):
        print("Ack")
    # print('Ping-' + str(count))
    # count += 1
    time.sleep(1)