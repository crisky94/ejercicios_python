# b. Escribe una función obtener_maximo_absoluto que reciba una lista de números y devuelva el valor absoluto más alto.
def obtener_maximo_absoluto(numeros):
    return max(abs(num) for num in numeros)
# abs = valor absoluto num es -1 lo convierte en 1

numeros = [ -2, 5, 7, -30, 45]