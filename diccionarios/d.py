# d. Creación de un diccionario de contactos
# Pide al usuario que ingrese nombres y números de teléfono, y almacénalos en un diccionario. Permite que el usuario ingrese varios contactos y luego imprime el diccionario completo.

contactos = {}

while True:
    nombre = input('Ingresa un nombre: (o "salir" para terminar)')
    if nombre == 'salir':
        break
    telefono = input('Ingresa el telefono: ')
    contactos[nombre] = telefono
# Salida esperada: {'Luis': '12345', 'Ana': '67890'}

print(contactos)