import random

numA = random.randint(1, 100)
numero = -1
while numero != numA:
    numero = int(input("Introduce un número: "))
    if numero > numA:
        print("Te pasaste")
    elif numero < numA:
        print("Te quedaste corto")

print(f"Felicidades, El numero es: {numA}")