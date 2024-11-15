# Crear un juego sencillo de "Piedra, Papel o Tijera" donde el jugador compita contra la computadora. El juego debe estar organizado en funciones para separar las distintas tareas.

# Función opcion_humano():

# Crea una función llamada opcion_humano() que permita al jugador elegir entre "piedra", "papel" o "tijera". La función debe validar que la opción ingresada sea válida (debe ser una de estas tres opciones). Si el jugador ingresa algo incorrecto, la función debe pedirle que ingrese de nuevo.
# Función opcion_computadora():

# Crea una función llamada opcion_computadora() que simule la elección de la computadora. La computadora debe elegir aleatoriamente entre "piedra", "papel" o "tijera".
# Función detectar_ganador():

# Crea una función llamada detectar_ganador() que reciba como parámetros la opción del humano y la opción de la computadora. La función debe comparar ambas opciones y devolver un mensaje indicando quién ha ganado ("Humano", "Computadora" o "Empate").
# Función jugar():

# Crea una función llamada jugar() que se encargue de coordinar el flujo del juego. Esta función debe:
# Llamar a opcion_humano() para obtener la elección del humano.
# Llamar a opcion_computadora() para obtener la elección de la computadora.
# Llamar a detectar_ganador() para determinar el ganador y mostrar el resultado.
# Preguntar al jugador si quiere jugar otra ronda.
# Requerimientos:

# Utiliza la función random.choice() para que la computadora haga su elección de manera aleatoria.
# Utiliza un bucle para permitir al jugador jugar varias rondas si lo desea.
# El juego debe seguir pidiendo opciones hasta que el jugador decida no jugar más.
import random


OPCIONES = ['piedra', 'papel', 'tijera']



def opcion_humano() -> str:
    while True:
        opcion = input(f"elige entre  {', '.join(OPCIONES)}:").lower()
        if opcion in OPCIONES:
            return opcion
        else:
            print("Opcion no valida")

def opcion_computadora() -> str:
    return random.choice(OPCIONES)


def detectar_ganador(humano: str, computadora: str) -> str:
    if humano == computadora:
        return "Empate."
    elif (humano == 'piedra' and computadora == 'tijera') or \
         (humano == 'papel' and computadora == 'piedra') or \
         (humano == 'tijera' and computadora == 'papel'):
        return "El humano ganó esta ronda."
    else:
        return "La computadora ganó esta ronda."

def mostrar_ganador_ronda(humano: str, computadora: str) -> None:
    print(f'\nHumano: {humano}')
    print(f'\nComputadora: {computadora}')
    print(detectar_ganador(humano, computadora))

def jugar() -> None:
    while True:
        humano = opcion_humano()
        computadora = opcion_computadora()
        mostrar_ganador_ronda(humano, computadora)
        if input('Jugar otra vez (s/n)').strip().lower() == 'n':
            print('\nGracias por jugar.')
            break
jugar()

