import turtle
import math
from turtle import *


def heart(x):
    return 15*math.sin(x)**3
def heart2(x):
    return(
        12*math.cos(x)-5*
        math.cos(2*x)-2*
        math.cos(3*x)-math.cos(4*x)
    )
speed(5999)
bgcolor('#e4e2be')
color('#e4e2be')
for i in range(6000):
    goto(heart(i)*20,heart2(i)*20)
    for j in range(5):
        color('#9f85af')
done()
