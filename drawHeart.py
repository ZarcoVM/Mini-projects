import math  # Importa la biblioteca math para usar funciones matemáticas, como sin() y cos().
from turtle import *  # Importa todas las funciones de la biblioteca turtle para dibujar.

def hearta(k):
    # Calcula la coordenada x del corazón usando una fórmula basada en seno.
    return 15 * math.sin(k)**3
