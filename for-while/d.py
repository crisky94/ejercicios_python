# d. Adivina el número
# Desarrolla un juego donde el programa elige un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. El programa debe usar un bucle while para permitir múltiples intentos.

# Pistas:

# Usa la biblioteca random y la función randint() para generar un número aleatorio.
# Proporciona retroalimentación al usuario si su intento es menor o mayor.
import random

num_aleatorio = random.randint(1, 100)
i = 0

while i < 5:
    num_usuario = int(input('Ingresa un número e intenta adivinar el número entre 1 y 100, tienes 5 intentos: '))
    if num_usuario < num_aleatorio:
        print(f'El numero ingresado {num_usuario} es menor.')
    elif num_aleatorio > num_usuario:
        print(f'El numero ingresado {num_usuario} es mayor.')
    else:
        print(f'El numero ingresado {num_usuario} es correcto.')
        break
    i += 1