#!/usr/bin/python
import socket, sys
from struct import *
 
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
	pack = s.recvfrom(20000)
	packet = pack[0] 
        data = packet[0:20]
        ip_header_data = unpack('!BBHHHBBH4s4s', data) 
        ip_version = ip_header_data[0] >> 4
	IHL = ip_header_data[0] & 0x0F
	diff_services = ip_header_data[1]
	total_length = ip_header_data[2] 
	id_ = ip_header_data[3]

	flags = ip_header_data[4] & 0xE000 >> 13
	TTL 	 = ip_header_data[5]
	protocol = ip_header_data[6]
	checksum = ip_header_data[7]
	source   = ip_header_data[8]
	destinat = ip_header_data[9]
	payload = packet[20:]


	print "Estructura del paquete"
	print "Version: %s  \n\rHeader lenght: %s"  %(ip_version,IHL)
	print "Diferentiated services: %s \n\rID: %s" %(diff_services, id_)
	print "Flags: %s \n\rTTL: %s \n\rProtocol: %s" %(flags,TTL,protocol)
	print "Checksum: %s \n\rIp_origen: %s \n\rIpdesrino: %s" %(checksum, socket.inet_ntoa(source),socket.inet_ntoa(destinat))
	print "Payload: %s" %(payload)

#nota: este programa solo recoge los paquetes entrantes
