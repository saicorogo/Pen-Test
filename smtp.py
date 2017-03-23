#!/usr/bin/python
import sys
from socket import *
# un puerto diferente a 25? 
if (len(sys.argv) == 4):
  print "verificacion de usuarios smtp"
  sys.exit(1)
  host = int(sys.argv[1])
  usuario = int(sys.argv[2])
  puerto = int(sys.argv[3]) 
if (len(sys.argv) < 3):
  puerto = 25 
  try:
    s=socket(AF_INET,SOCK_STREAM)
    s.connect((sys.argv[2],25))
    s.recv(1024)	
    s.send('VRFY '+sys.argv[2]+'\r\n')
    if '252' in s.recv(1024):
      print "se encuentra"
    else:
      print "no esta"
    s.close()
  except:
    print "Error"
