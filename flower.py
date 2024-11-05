from turtle import *
import turtle
import math

tracer(2)
h = 0
bgcolor('black')
pensize(2)
color('yellow')

for i in range(195):
    h += 0.006
    lt(179)
    backward(i * 0.1)
    circle(i * 0.3, 120)
    rt(14)
    forward(i * 0.1)
    circle(i * 0.3, 120)
turtle.shape('turtle')
turtle.pencolor('orangered')
turtle.fillcolor('orange')
