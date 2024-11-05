# h. Verificar la longitud de una palabra
# Escribe un programa que pida al usuario una palabra y verifique su longitud:

# Menos de 4 caracteres: “Palabra corta.”
# Entre 4 y 8 caracteres: “Palabra de longitud media.”
# Más de 8 caracteres: “Palabra larga.”

palabra = input('Ingresa una palabra: ')
mensaje = ''

if 4 > len(palabra):
    mensaje = 'Palabra corta'
elif 4 <= len(palabra) <= 8:
    mensaje = 'Palabra de longitud media'
else:
    mensaje = 'Palabra larga'

print(f'{mensaje}')


# print(f'{progrmacion.len()}')