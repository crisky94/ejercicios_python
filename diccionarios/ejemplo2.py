# Crea un diccionario que contenga nombres y edades de 5 personas. Luego, crea un nuevo diccionario que contenga solo aquellas personas cuya edad sea mayor a 30 años, utilizando comprensión de diccionarios.

personas = [
    {'nombre': 'Juan', 'edad': 44},
    {'nombre': 'Carlos', 'edad': 30},
    {'nombre': 'Maria', 'edad': 25},
    {'nombre': 'Juana', 'edad': 50},
]

for persona in personas:
    if persona['edad'] > 30:
        print(persona)