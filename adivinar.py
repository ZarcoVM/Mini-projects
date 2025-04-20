
import random     
# Genera un número aleatorio entre 1 y 100
numA = random.randint(1, 100)
# Inicializa la variable para almacenar el
 número ingresado por el usuario
# y el contador de intentos
numero = -1
intentos = 0 
# Bucle que continúa hasta que el usuario
 adivine el número 
while numero != numA:
    # Solicita al usuario que introduzca un número
    numero = int(input("Introduce un número: "))
    # Incrementa el contador de intentos
    intentos += 1
 # Verifica si el número ingresado es mayor o menor que el número aleatorio
    if numero > numA:
        print("Te pasaste")
    elif numero < numA:
        print("Te quedaste corto")

# Cuando el número es correcto, muestra un mensaje de felicitación y el número de intentos
print(f"Felicidades, el número es: {numA}. Lo lograste en {intentos} intentos.")
