# b. Contar vocales
# Crea un programa que pida al usuario una frase y cuente cuántas vocales (a, e, i, o, u) hay en la frase utilizando un bucle for.

# Pistas:

# Usa una lista o cadena que contenga las vocales y verifica cada carácter de la frase para ver si está en esa lista.

frase = input('Ingresa una frase: ')
vocales = 0

for v in frase:
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        vocales += 1

print(f'El total de vocales de la frase ingresada es: {vocales} ')