# j. Verificar condiciones meteorológicas complejas
# Pide al usuario la temperatura y el nivel de humedad. Luego, determina el tipo de clima:

# Si la temperatura es menor a 10°C y la humedad es mayor al 80%, indica "Frío y húmedo".
# Si la temperatura es menor a 10°C y la humedad es menor o igual a 80%, indica "Frío y seco".
# Si la temperatura está entre 10°C y 25°C y la humedad es mayor al 60%, indica "Templado y húmedo".
# Si la temperatura está entre 10°C y 25°C y la humedad es menor o igual a 60%, indica "Templado y seco".
# Si la temperatura es mayor a 25°C, verifica si la humedad es mayor a 50% para indicar "Caluroso y húmedo" o "Caluroso y seco" en caso contrario.

temperatura = float(input('Ingresa la temperatura en °C: '))
humedad = float(input('Ingresa el nivel de humedad (%): '))
mensaje = ''

if temperatura < 10 and humedad > 80:
    mensaje = 'Frío y húmedo'
elif temperatura < 10 and humedad <= 80:
    mensaje = 'Frío y seco'
elif 10 <= temperatura <= 25 and humedad > 60:
    mensaje = 'Templado y húmedo'
elif 10 <= temperatura <= 25 and humedad <= 60:
    mensaje = 'Templado y seco'
elif temperatura > 25 and humedad > 50:
    mensaje = 'Caluroso y húmedo'
else:
    mensaje = 'Caluroso y seco'

print(mensaje)