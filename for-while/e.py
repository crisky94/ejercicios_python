# e. Contar espacios
# Pide al usuario que ingrese un texto y cuenta cuántos espacios hay utilizando un bucle for.

texto = input('Ingresa un texto: ')
count = 0

for t in texto:
    if t == ' ':
        count += 1
print(count)
# Pistas:

# Recuerda que el objeto str es un iterable.