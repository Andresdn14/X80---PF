import x80
from robot import robot

def mov(robot,faceD):
    destiny = faceD
    face = robot.face
    print("faceR = ",face)
    
    print("faceD = ",destiny)
    rid = robot.id


#----------------- 0 -------------------#
    if face == 0:
        x80.stop(rid)


#----------------- 1 -------------------#
    if face == 1:
        if destiny == 1:
            print("0º")
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny
        if destiny == 2:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
            print("cara del robot = ",robot.face) 
        if destiny == 3:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 5:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 6:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 7:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            print("La del error")
            robot.face = destiny 
        if destiny == 8:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
    print("cara del robot afuera = ",robot.face)

#----------------- 2 -------------------#
    if face == 2:
        if destiny == 1:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward2(rid,1) 
            robot.face = destiny 
        if destiny == 2:
            print("0º")
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 3:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 5:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 6:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 


#----------------- 3 -------------------#
    if face == 3:
        if destiny == 1:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny 
        if destiny == 2:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 3:
            print("0º")
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 5:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 6:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 


#----------------- 4 -------------------#
    if face == 4:
        if destiny == 1:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny
        if destiny == 2:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 3:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("0º")
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 5:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 6:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 7:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 


#----------------- 5 -------------------#
    if face == 5:
        if destiny == 1:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny 
        if destiny == 2:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 3:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 4:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 5:
            print("0º")
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 6:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 


#----------------- 6 -------------------#
    if face == 6:
        if destiny == 1:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward2(rid,1) 
            robot.face = destiny
        if destiny == 2:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 3:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 5:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 6:
            print("0º")
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 


#----------------- 7 -------------------#
    if face == 7:
        if destiny == 1:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny
        if destiny == 2:
            print("90º derecha") 
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 3:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 4:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 5:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 6:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("0º")
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 8:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny


#----------------- 8 -------------------#
    if face == 8:
        if destiny == 1:
            print("45º derecha")
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward2(rid,1)
            robot.face = destiny 
        if destiny == 2:
            print("90º derecha")
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 
        if destiny == 3:
            print("90º derecha")
            print(" 45º derecha")
            x80.turn90(rid,0)
            x80.turn45(rid,0)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny
        if destiny == 4:
            print("90º derecha")
            print("90 derecha")
            x80.turn90(rid,0)
            x80.turn90(rid,0)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 5:
            print("90º IZQUIERDA")
            print("45º IZQUIERDA")
            x80.turn90(rid,1)
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 6:
            print("90º IZQUIERDA")
            x80.turn90(rid,1)
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny
        if destiny == 7:
            print("45º IZQUIERDA")
            x80.turn45(rid,1)
            print("Forward Corto")
            x80.forward(rid,1)
            robot.face = destiny 
        if destiny == 8:
            print("0º")
            print("Forward Largo")
            x80.forwardL(rid,1)
            robot.face = destiny 