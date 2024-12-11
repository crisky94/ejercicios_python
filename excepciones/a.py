# a. División segura
# Escribe una función dividir(a, b) que maneje divisiones por cero lanzando una excepción ZeroDivisionError.

a = int(input('Ingresa un numero: '))
b = int(input('Ingresa un numero: '))

def dividir(a, b):
    try:
        return a / b
    except  ZeroDivisionError:
        print('No se puede dividir por zero')

result = dividir(a, b)
print(result)
