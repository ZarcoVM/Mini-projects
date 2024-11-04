import math  # Importa la biblioteca math para usar funciones matemáticas, como sin() y cos().
from turtle import *  # Importa todas las funciones de la biblioteca turtle para dibujar.

def hearta(k):
    # Calcula la coordenada x del corazón usando una fórmula basada en seno.
    return 15 * math.sin(k)**3
    
def heartb(k):
    # Calcula la coordenada y del corazón usando una fórmula basada en coseno.
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

