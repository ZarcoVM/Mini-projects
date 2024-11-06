from turtle import *
import turtle
import math

# Reduce la velocidad de dibujo para que sea más fluido
tracer(2)

# Color de fondo negro
bgcolor('black')

# Configuración inicial de la pluma
pensize(2)
color('yellow')

# Dibujar un patrón de líneas y círculos con un giro progresivo
h = 0  # Contador de incremento
for i in range(195):
    h += 0.006  # Incremento para posibles variaciones de color
    lt(179)  # Girar la tortuga hacia la izquierda 179 grados
    backward(i * 0.1)  # Mover hacia atrás una distancia que aumenta con cada iteración
    circle(i * 0.3, 120)  # Dibujar un arco de círculo
    rt(14)  # Girar hacia la derecha 14 grados
    forward(i * 0.1)  # Avanzar una distancia que también crece con cada iteración
    circle(i * 0.3, 120)  # Otro arco de círculo
