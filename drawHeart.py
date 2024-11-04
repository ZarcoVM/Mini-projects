import math  # Importa la biblioteca math para usar funciones matemáticas, como sin() y cos().
from turtle import *  # Importa todas las funciones de la biblioteca turtle para dibujar.

def hearta(k):
    # Calcula la coordenada x del corazón usando una fórmula basada en seno.
    return 15 * math.sin(k)**3
    
def heartb(k):
    # Calcula la coordenada y del corazón usando una fórmula basada en coseno.
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # Establece la velocidad máxima de dibujo.
bgcolor("black")  # Cambia el color de fondo de la ventana a negro.

for i in range(6000):  # Repite el bucle 6000 veces para crear el dibujo completo.
    goto(hearta(i) * 20, heartb(i) * 20)  # Mueve la tortuga a las coordenadas calculadas y las amplifica por 20.

for j in range(5):
        color("red")  # Cambia el color del "lápiz" a rojo (este bucle no es necesario aquí).

    goto(0, 0)  # Regresa la tortuga al origen después de cada movimiento, lo cual afecta el dibujo final.

done()  # Termina el dibujo y mantiene la ventana abierta.
