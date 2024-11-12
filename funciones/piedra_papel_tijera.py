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

OPCIONES = ['piedra', 'papel', 'tijera']


