# Se tiene una lista con tres elementos: [1, 2, 3]. Solicita al usuario que ingrese un número entero. El programa debe intentar realizar dos operaciones con el número proporcionado:

# Convertir el valor ingresado en un número entero.
# Acceder a un índice de la lista usando el número proporcionado.

# Requisitos:

# Si el usuario ingresa un valor que no pueda ser convertido a un número entero (por ejemplo, una cadena de texto), el programa debe capturar el error y mostrar el mensaje:
# "Error: Debes introducir un número entero."

# Si el número ingresado es un índice fuera del rango de la lista (por ejemplo, si el número es 5), el programa debe capturar el error y mostrar el mensaje:
# "Error: El índice proporcionado está fuera del rango de la lista."

# Si ocurre cualquier otro error inesperado, el programa debe capturar el error y mostrar un mensaje genérico indicando que ocurrió un error, sin especificar detalles del tipo de error. El mensaje debe ser:
# "Se ha producido un error inesperado: {mensaje del error}"

lista = [1, 2, 3]

def proceso():
    numero = int(input('Ingresa un indeice entre 0 y 2 inclusive: '))
    print(lista[numero])

try:
    proceso()
except ValueError:
    print("Error: Debes introducir un número entero.")
except IndexError:
    print("Error: El índice proporcionado está fuera del rango de la lista.")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")