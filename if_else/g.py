# g. Determinar si un número es divisible entre 2 y entre 3
# Solicita al usuario un número y verifica si es divisible entre 2, entre 3 o entre ambos.

numero = float(input('Ingresa un número: '))
mensaje = ''

if numero % 2 == 0  and numero % 3 == 0:
    mensaje = 'es divisible entre 2 y entre 3'
elif numero % 2 == 0 :
    mensaje = 'es divisible entre 2'
elif numero % 3 == 0:
    mensaje = 'es divisible entre 3'
else:
    mensaje = 'no es divisible ni entre 2, ni entre 3'

print(f'El número {mensaje}')