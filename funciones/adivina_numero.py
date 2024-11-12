# Crear una función que permita comparar un número secreto con el intento de un jugador. La función debe devolver un valor que indique si el intento del jugador es mayor, menor o igual al número secreto.

# Crea una función llamada comparar_numeros que reciba dos parámetros: el numero_secreto (un número entero) y el intento (un número entero que representa el intento del jugador).
# La función debe devolver:
# -1 si el intento es menor que el numero_secreto.
# 1 si el intento es mayor que el numero_secreto.
# 0 si el intento es igual al numero_secreto.
# Una vez creada la función, implementa un juego dentro de un bucle while True, donde el jugador deberá seguir intentando adivinar el número secreto hasta que lo logre. En cada intento, la función debe ser llamada y el juego debe indicarle al jugador si debe intentar con un número mayor o menor.
# Utiliza input() para que el jugador ingrese su intento. El juego debe seguir pidiendo intentos hasta que el jugador adivine el número.

import random 


MENSAJES = {
    0: 'Ganastes!',
    1: 'El numero debe ser menor',
    -1: 'El numero debe ser mayor'
}

def comparar_numeros(numero_secreto: int, intento: int) -> int:
    if intento < numero_secreto:
        return -1
    elif intento > numero_secreto:
        return 1
    else:
        return 0

def jugar():
    numero_secreto = random.randint(1, 100)
    while True:
        intento = int(input('Adivina el numero: '))
        resultado = comparar_numeros(numero_secreto, intento)
        print(MENSAJES[resultado])
        if resultado == 0:
            break
jugar()