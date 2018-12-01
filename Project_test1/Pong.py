from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=868300000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    message = s.recv(64)
    message = message.decode("hex")
    if message:
      print("message =", message)
    time.sleep(1)