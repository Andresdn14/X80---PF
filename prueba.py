import checksum
import suspendRes
import moveServo
import motorFeedback
import socket
#suspendRes.suspendRes('5e02','01','00','1e','01','5e0d','00')
#moveServo.moveServo('5e02','01','00','1c','03','010009','5e0d')
#lectura=motorFeedback.motorFeedback('5e02','01','00','7b','01','01','5e0d')
#print(lectura)
def AdelanteVelocidad():
	pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe 2c 01 00 80 00 80 00 80 00 80 05 5e0d')
	UDP_PORT=10001
	UDP_IP='192.168.0.201'
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()

#AdelanteVelocidad()


def girar90 ():

	pack=bytes.fromhex('5e02 01 00 1b 0c 4f 2c 73 4b 00 80 00 80 00 80 00 80 a0 0f  58 5e0d')
	UDP_PORT=10001
	UDP_IP='192.168.0.202'
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()

#girar90()

def atras():
	pack=bytes.fromhex('5e02 01 00 1b 0c 2c 01 d4 fe 00 80 00 80 00 80 00 80 b2 5e0d')
	UDP_PORT=10001
	UDP_IP='192.168.0.202'
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
#atras()

def izquierda():
	pack=bytes.fromhex('5e02 01 00 1b 0c 2c 01 2c 01 00 80 00 80 00 80 00 80 91 5e0d')
	UDP_PORT=10001
	UDP_IP='192.168.0.202'
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
#izquierda()

def derecha():
	pack=bytes.fromhex('5e02 01 00 1b 0c d4 fe d4 fe 00 80 00 80 00 80 00 80 26 5e0d')
	UDP_PORT=10001
	UDP_IP='192.168.0.202'
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.sendto(pack,(UDP_IP,UDP_PORT))
	s.close()
#derecha()

