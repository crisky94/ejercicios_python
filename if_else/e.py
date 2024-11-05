# e. Clasificación de temperaturas
# Escribe un programa que pida al usuario una temperatura en grados Celsius entre -100 y 100, y la clasifique en:

# Menor a 0: "Frío extremo"
# Entre 0 y 15: "Frío"
# Entre 16 y 25: "Templado"
# Mayor a 25: "Calor"

temperatura = float(input('Ingresa la temperatura en Celsius: '))
mensaje = ''
if 0 > temperatura:
    mensaje = 'frío extremo'
elif 0 <= temperatura <= 15:
    mensaje = 'frío'
elif 16 <= temperatura <= 25:
    mensaje = 'templada'
else:
    mensaje = 'calor'


print(f'La temperatura es {mensaje}')