# Simulación de lanzamiento de dado:

# Crea una función llamada lanzar_dado() que no reciba parámetros y devuelva un número aleatorio entre 1 y 6, simulando el lanzamiento de un dado.
# Utiliza la función random.randint() para obtener el número aleatorio.
# Juego de competencia:

# Crea una función llamada jugar() donde el jugador y la computadora lanzan un dado.
# El jugador debe ingresar el número de veces que desea lanzar el dado. En cada intento, el jugador lanzará el dado y la computadora también lo hará de forma aleatoria.
# La función jugar() debe imprimir los resultados de cada lanzamiento, indicando quién ganó cada ronda (jugador o computadora) y mostrar el puntaje total después de todas las rondas.
# Al final del juego, la función debe imprimir quién ganó (si el jugador tiene más puntos que la computadora, el jugador gana; si es al revés, gana la computadora).
# El juego se detendrá cuando el jugador decida no continuar.
# Requerimientos:

# Utiliza la función lanzar_dado() para simular el lanzamiento del dado tanto para el jugador como para la computadora.
# Usa un bucle para que el jugador decida cuántas rondas jugar.
# Debes manejar correctamente el puntaje y la impresión de los resultados de cada ronda.
# Ejemplo de salida:

# Ronda 1
# Humano: 1
# Computadora: 1
# Empate.

# Ronda 2
# Humano: 4
# Computadora: 4
# Empate.

# Ronda 3
# Humano: 5
# Computadora: 4
# El humano ganó esta ronda.

# Ronda 4
# Humano: 2
# Computadora: 6
# La computadora ganó esta ronda.

# Puntaje final
# Humano: 1
# Computadora: 1
# El juego terminó en empate.

import random

def lanzar_dado() -> int:
    return random.randint(1, 6)

def jugar() -> None:
    while True:
        rondas = int(input('¿Cuántas rondas quieres jugar? '))
        puntaje_humano = 0
        puntaje_computadora = 0

        for ronda in range(1, rondas + 1):
            humano = lanzar_dado()
            computadora = lanzar_dado()
            mostrar_resultado_ronda(ronda, humano, computadora)
            if humano > computadora:
                puntaje_humano += 1
            elif humano < computadora:
                puntaje_computadora += 1

        mostrar_final_juego(puntaje_humano, puntaje_computadora)

        continuar = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Gracias por jugar!")
            break

def mostrar_resultado_ronda(ronda: int, humano: int, computadora: int) -> None:
    print(f'\nRonda {ronda}')
    print(f'Humano: {humano}')
    print(f'Computadora: {computadora}')
    mostrar_ganador_ronda(humano, computadora)

def mostrar_ganador_ronda(humano: int, computadora: int) -> None:
    if humano > computadora:
        print('El humano ganó esta ronda.')
    elif computadora > humano:
        print('La computadora ganó esta ronda.')
    else:
        print('Empate en esta ronda.')

def mostrar_ganador_juego(puntaje_humano: int, puntaje_computadora: int) -> None:
    if puntaje_humano > puntaje_computadora:
        print('El humano ganó el juego.')
    elif puntaje_computadora > puntaje_humano:
        print('La computadora ganó el juego.')
    else:
        print('El juego terminó en empate.')

def mostrar_final_juego(puntaje_humano: int, puntaje_computadora: int) -> None:
    print('\nPuntaje final:')
    print(f'Humano: {puntaje_humano}')
    print(f'Computadora: {puntaje_computadora}')
    mostrar_ganador_juego(puntaje_humano, puntaje_computadora)
jugar()