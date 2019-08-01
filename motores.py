import checksum
import socket
#import convert
import time
def encoder_DC(motor,posision):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDseting='07'
	DIDcontrol='03'
	lenghcontrol='03'
	lenghseting='03'
	dataseting1='0d'+motor+'02'
	dataseting2='0e'+motor+'01'
	datacontrol=motor+posision
	ETX='5e0d'
	checkseting1=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting1)
	checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	packetseting1=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting1+checkseting1+ETX)
	packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	UDP_IP = "192.168.0.201"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting1, (UDP_IP, UDP_PORT))
	s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()


def PWM_DC(motor,pwm,pol):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDcontrol='05'
	DIDseting='07'
	lenghcontrol='03'
	lenghseting='03'
	datacontrol=motor+pwm
	dataseting='0e'+motor+'00'
	#dataseting2='06'+motor+pol
	ETX='5e0d'
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	checkseting=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting)
	#checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	packetseting=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting+checkseting+ETX)
	#packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	UDP_IP = "192.168.0.201"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting, (UDP_IP, UDP_PORT))
	#s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()

def all_PWM_DC(pwm1,pwm2,pol):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDcontrol='06'
	DIDseting='07'
	lenghcontrol='0c'
	lenghseting='03'
	datacontrol=pwm1+pwm2+'0000'+'0000'+'0000'+'0000'
	dataseting='0e'+'01'+'00'
	dataseting2='0e'+'00'+'00'
	dataseting3='060001'
	dataseting4='060101'
	ETX='5e0d'
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	checkseting=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting)
	checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkseting3=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting3)
	checkseting4=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting4)

	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	packetseting=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting+checkseting+ETX)
	packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetseting3=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting3+checkseting3+ETX)
	packetseting4=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting4+checkseting4+ETX)
	UDP_IP = "192.168.0.201"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting, (UDP_IP, UDP_PORT))
	s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetseting3, (UDP_IP, UDP_PORT))
	s.sendto(packetseting4, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()

def mover_velocidad(motor,velocidad):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDseting='07'
	DIDcontrol='1a'
	lenghcontrol='03'
	lenghseting='03'
	dataseting1='0d'+motor+'02'
	dataseting2='0e'+motor+'02'
	datacontrol=motor+velocidad
	ETX='5e0d'
	checkseting1=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting1)
	checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	packetseting1=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting1+checkseting1+ETX)
	packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	UDP_IP = "192.168.0.202"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting1, (UDP_IP, UDP_PORT))
	s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()	

def mover_servo(servo,posision):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDcontrol='1c'
	lenghcontrol='03'
	datacontrol=servo+posision
	ETX='5e0d'
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	UDP_IP = "192.168.0.202"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()

def setting_parametros():
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDcontrol='06'
	DIDseting='07'
	lenghseting='03'
	dataseting='0d'+'00'+'00'
	#dataseting2='0e'+'00'+'00'
	dataseting3='06'+'00'+'01'
	dataseting4='0601ff'
	ETX='5e0d'
	checkseting=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting)
	#checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkseting3=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting3)
	checkseting4=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting4)

	packetseting=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting+checkseting+ETX)
	#packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetseting3=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting3+checkseting3+ETX)
	packetseting4=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting4+checkseting4+ETX)
	UDP_IP = "192.168.0.201"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting, (UDP_IP, UDP_PORT))
	#s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetseting3, (UDP_IP, UDP_PORT))
	s.sendto(packetseting4, (UDP_IP, UDP_PORT))
	s.close()

def all_encoder_DC(posision1,posision2):
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDseting='07'
	DIDcontrol='04'
	lenghcontrol='0c'
	lenghseting='03'
	dataseting1='0d'+'00'+'02'
	dataseting2='0e'+'00'+'01'
	dataseting3='0d'+'01'+'02'
	dataseting4='0e'+'01'+'01'
	datacontrol=posision1+posision2+posision1+posision1+posision1+posision1
	ETX='5e0d'
	checkseting1=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting1)
	checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkseting3=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting3)
	checkseting4=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting4)
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	packetseting1=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting1+checkseting1+ETX)
	packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetseting3=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting3+checkseting3+ETX)
	packetseting4=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting4+checkseting4+ETX)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	UDP_IP = "192.168.0.201"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting1, (UDP_IP, UDP_PORT))
	s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetseting3, (UDP_IP, UDP_PORT))
	s.sendto(packetseting4, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()

def girar_90():
	STX='5e02' 
	RID='01'
	reservet='00'
	DIDseting='07'
	DIDcontrol='04'
	lenghcontrol='0c'
	lenghseting='0b'
	dataseting1='07'+'00'+'01'+'e8'+'03'+'02'+'05'+'00'+'03'+'10'+'27'
	dataseting2='07'+'01'+'01'+'e8'+'03'+'02'+'05'+'00'+'03'+'10'+'27'
	datacontrol='a17b'+'4514'+'0080'+'0080'+'0080'+'0080'
	ETX='5e0d'
	checkseting1=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting1)
	checkseting2=checksum.checksum(RID,reservet,DIDseting,lenghseting,dataseting2)
	checkcontrol=checksum.checksum(RID,reservet,DIDcontrol,lenghcontrol,datacontrol)
	packetseting1=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting1+checkseting1+ETX)
	packetseting2=bytes.fromhex(STX+RID+reservet+DIDseting+lenghseting+dataseting2+checkseting2+ETX)
	packetcontrol=bytes.fromhex(STX+RID+reservet+DIDcontrol+lenghcontrol+datacontrol+checkcontrol+ETX)
	UDP_IP = "192.168.0.202"
	UDP_PORT = 10001
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packetseting1, (UDP_IP, UDP_PORT))
	s.sendto(packetseting2, (UDP_IP, UDP_PORT))
	s.sendto(packetcontrol, (UDP_IP, UDP_PORT))
	s.close()






