# f. Crea una clase Estudiante que almacene el nombre y las calificaciones de un estudiante. Luego, crea una lista de objetos Estudiante y calcula el promedio de calificaciones de todos los estudiantes.

class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones
    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

estudiantes = [
    Estudiante('Paco', [5, 6, 7]),
    Estudiante('Manuel', [7, 8, 9]),
    Estudiante('Lola', [8, 9, 10])
]

promedios_individuales = [est.promedio() for est in estudiantes]
promedio_general = sum(promedios_individuales) / len(estudiantes)


for estudiante, promedio in zip(estudiantes, promedios_individuales):
    print(f"{estudiante.nombre}: {promedio:.2f}")


print(f"\nPromedio general de todos los estudiantes: {promedio_general:.2f}")