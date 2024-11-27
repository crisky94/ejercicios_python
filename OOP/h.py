# h. Crea una clase Curso que gestione una lista de estudiantes y permita calcular el promedio del curso. Utiliza la clase Estudiante del ejercicio f.

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

class Curso:
    def __init__(self, estudiantes):
        self.estudiantes = []
    def promedio_curso(self)
