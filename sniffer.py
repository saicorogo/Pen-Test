#!/usr/bin/python
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
  print s.recvfrom(65565)
#nota: solo detecta o recoge los paquetes entrantes.
