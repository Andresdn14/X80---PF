import socket
STX='5e02' 
RID='01'
reservet='00'
DID='05'
lengh='03'
data='00000000'
checksun='65'
ETX='5e0d'
packet=bytes.fromhex(STX+RID+reservet+DID+lengh+data+checksun+ETX)
UDP_IP = "192.168.0.201"
UDP_PORT = 10001
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(packet, (UDP_IP, UDP_PORT ))
#while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
 #   mensaje = raw_input("Mensaje a enviar >> ")

    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
  #  s.send(mensaje)

    #Si por alguna razon el mensaje es close cerramos la conexion
   # if mensaje == "close":
    #    break
#Imprimimos la palabra Adios para cuando se cierre la conexion
#print "Adios."

#Cerramos la instancia del objeto servidor
s.close()