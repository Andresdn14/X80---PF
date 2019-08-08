from cell import cell
from robot import robot
import rotation



def movement(rob,rx,ry):
    faceD = 0
    length = len(rx)
    for i in range(length) :
        print(rx[i],ry[i])
        
        faceD = whatFace(rob,rx[i],ry[i],faceD)
        print("-------------------------- MOVIMIENTO = ", i)
        print("before rot = ",faceD)
        rotation.mov(rob,faceD)
        rob.x = rx[i]
        rob.y = ry[i]
        
            

        
    print("final face of R = ",rob.x,rob.y)

def whatFace(rob,dx,dy,faceD):
    ox = rob.x
    oy = rob.y
    if (ox == dx) and (oy == dy):
        faceD = 0
    if (ox == dx) and (dy > oy):
        faceD = 1
    if (dx > ox) and (dy > oy):
        faceD = 2
    if (dx > ox) and (dy == oy):
        faceD = 3
    if (dx > ox) and (dy < oy):
        faceD = 4
    if (dx == ox) and (dy < oy):
        faceD = 5
    if (dx < ox) and (dy < oy):
        faceD = 6
    if (dx < ox) and (dy == oy):
        faceD = 7
    if (dx < ox) and (dy > oy):
        faceD = 8
    print("faceD calc = ", faceD)
    return faceD

rx,ry = [1,1,0,1,0,0],[1,2,2,3,4,3]

x80 = robot()
x80.x = 0
x80.y = 0
x80.face = 1
x80.id = 0

movement(x80,rx,ry)

