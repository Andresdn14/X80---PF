import x80
import time


x80.enableMotorServo(0,1)
x80.stop(1)
x80.forward2(1,1)
x80.turn90(1,1)
x80.forward2(1,1)
x80.turn90(1,0)
x80.forward2(1,2)
x80.turn90(1,0)
x80.forward2(1,2)
x80.turn90(1,0)
x80.forward2(1,2)
x80.turn90(1,0)
x80.forward2(1,1)
x80.turn90(1,1)
x80.forward2(1,1)
x80.turn90(1,0)
x80.turn90(1,0)
x80.stop(1)