#!/usr/bin/python
import sys
import subprocess
#import Popen, PIPE

class Red():
  direccion={'ip':'','mascara':''}
  def __init__(self, ip, mascara):
    
    self.direccion['ip']=ip
    self.direccion['mascara']=mascara
  
  def calculaNumeroHost(self):

    netID=""
    numHosts=0
    octetosCompletos=0
    octetosIP=self.direccion['ip'].split('.')
    octetosMascara=self.direccion['mascara'].split('.')
    for octetoActual in  octetosMascara:
      if int(octetoActual)==255:
        netID=netID+octetosIP[octetosCompletos]+'.'
        octetosCompletos=octetosCompletos+1
        next
      else:
        ceros=8
        for digito in bin(int(octetosMascara[octetosCompletos]))[2:]:
          if digito=='1': ceros=ceros-1
          else:break 
        numHosts=2**((3-octetosCompletos)*8+ceros)-2
        netID=netID+str(int(octetosIP[octetosCompletos]) & int(octetoActual))
        while octetosCompletos<3:
          netID=netID + '.0'
          octetosCompletos=octetosCompletos+1
        break
    return numHosts,netID
    
  def generaListaHost(self):
    ips=[]
    numHosts,netID=self.calculaNumeroHost()
    red=netID.split('.')
    while numHosts>0:
      red[3]=str( int(red[3])+1 )
      ips.append(red[0]+'.'+red[1]+'.'+red[2]+'.'+red[3])
      if red[3]=='255':
        if red[2]=='255':
          if red[1]=='255':
            red[0]=str(int(red[0])+1)
            red[1]='0'
            red[2]='0'
            red[3]='0'
          else:
            red[1]=str(int(red[1])+1)
          red[2]='0'
          red[3]='0'
        else:
          red[2]=str(int(red[2])+1)
        red[3]='0'
      numHosts=numHosts-1
    return ips
  def ping(self):
    for host in self.generaListaHost():
      cmd = "ping -c 1"+host
      ps = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
      code=str(ps.stdout.readlines())
      #return process.returncode == 0  
      if code.find("+1 error") < 0:
        print str(host)+ "activo"

if len(sys.argv) == 3:
  host=str(sys.argv[1])
  netmask=str(sys.argv[2])
  scan=Red(host,netmask)
else:
  print "  Error : "+str(sys.argv[0])+"debes agregar la [ip] y la [mascara] "

  exit()
scan.ping()   
