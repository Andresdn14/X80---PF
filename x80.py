
import socket
import checksum
import time

#ESTA ES LA "LIBRERIA" DEL ROBOT SOLO ES INCLUIR TODAS LAS FUNCIONES AQUÍ E IMPORTARLA EN UN ARCHIVO Y YA.

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP_IP = ""
UDP_PORT = 0
STX = "5e02"
RID = "01"
ETX = "5e0d"
reservet = "00"



def setIP(robot):
#"CALL" GLOBAL VARIABLES
	global UDP_IP
	global UDP_PORT
#CHECK ROBOT AND SET IP & PORT
	if robot == 0 :
		UDP_IP = "192.168.0.201"
		UDP_PORT = 10001
	if robot == 1:
		UDP_IP = "192.168.0.202"
		UDP_PORT = 10001	



def enableMotorServo(robot,sw):
#"CALL" GLOBAL VARIABLES
	global STX
	global RID
	global ETX
	global reservet
#FUNCTION LOCAL VARIABLES
	DID = "1e"
	lengh = "01"
#SWITCH FOR DATA
	if sw == 0:
		data='00'
	else:
		data='01'
#CHECKSUM AND PACKET FOR TX
	check=checksum.checksum(RID,reservet,DID,lengh,data)
	packet=bytes.fromhex(STX+RID+reservet+DID+lengh+data+check+ETX)
#IP SET AND SENDING
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(packet, (UDP_IP, UDP_PORT))
	s.close()






	

def turn90L(robot):
	pack=bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
	time.sleep(1)
	stop(robot)
	time.sleep(0.5)
	s.close()

def turn90(robot,lr):
	if lr == 0:
		#DERECHA
		pack =  bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	else:
		#IZQUIERDA
		pack = bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')

	#pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
	time.sleep(1)
	stop(robot)
	time.sleep(0.5)
	s.close()


def turn45(robot,lr):
	if lr == 0:
		#DERECHA
		pack =  bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	else:
		#IZQUIERDA
		pack = bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')

	#pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
	time.sleep(0.5)
	stop(robot)
	time.sleep(0.5)
	s.close()




def stop(robot):
	velData = '00000000'
	startOfPack = '5e 02 01 00 1b 0c'
	endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
	pack=bytes.fromhex(startOfPack+velData+endOfPack)
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()

def forward(robot,velocity):
	#SWITCH FOR DATA
	velData = "0"
	if velocity == 0:
		velData = '00000000'
	if velocity == 1:
		velData = 'd7ff2900'
	if velocity == 2:
		velData = 'd4fe2c01'
	if velocity == 3:
		velData = '6afd9602'
	if velocity == 4:
		velData = '86fc7a03'
	if velocity == 5:
		velData = '50fbb004'
	if velocity == 6:
		velData = '46ffba00'
	startOfPack = '5e 02 01 00 1b 0c'
	endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
	pack=bytes.fromhex(startOfPack+velData+endOfPack)
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()

def forward2(robot,distance):
	#SWITCH FOR DATA
	velData = 'd4fe2c01'
	startOfPack = '5e 02 01 00 1b 0c'
	endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
	pack=bytes.fromhex(startOfPack+velData+endOfPack)
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	time.sleep(1.6*distance)
	stop(robot)
	s.close()

def forwardL(robot,distance):
	#SWITCH FOR DATA
	velData = 'd4fe2c01'
	startOfPack = '5e 02 01 00 1b 0c'
	endOfPack = '00 80 00 80 00 80 00 80 05 5e 0d'
	pack=bytes.fromhex(startOfPack+velData+endOfPack)
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	time.sleep(2.263*distance)
	stop(robot)
	s.close()

def backward(robot):
	pack=bytes.fromhex('5e02 01 00 1b 0c 2c 01 d4 fe 00 80 00 80 00 80 00 80 b2 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()


def left(robot):
	pack=bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
#izquierda()

def right(robot):
	pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	setIP(robot=robot)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
#derecha()




#enableMotorServo(1,"0")
#forward(1,0)
#turn90(1)


