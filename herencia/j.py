# j. Sistema de Evaluación con Ponderación: Crea una dataclass Evaluacion que almacene las notas y ponderaciones de un estudiante. Calcula el promedio ponderado en una clase CalculadoraPromedio.

from dataclasses import dataclass
from typing import List

@dataclass
class Evaluacion:
    nombre: str
    notas: List[float]
    ponderaciones: List[float]

    def __post__init__(self):
        if len(self.notas) != len(self.ponderaciones):
            raise ValueError('El número de notas y ponderaciones debe ser igual.')
        if not all(0 <= p <= 1 for p in self.ponderaciones):
            raise ValueError('Las ponderaciones deben estar entre 0 y 1.')
        if sum(self.ponderaciones) != 1:
            raise ValueError('La suma de las ponderaciones debe ser exactamente 1.')
        
class CalculadoraPromedio:
    @staticmethod
    def calcular_promedio_ponderado(evaluacion: Evaluacion):
        promedio = sum(nota * peso for nota, peso in zip(evaluacion.notas, evaluacion.ponderaciones))
        return promedio
    

try:
    evaluacion = Evaluacion(
        nombre='Juan Lopez',
        notas=[85, 90, 78],
        ponderaciones=[0.4, 0.4, 0.2],
    )

    promedio = CalculadoraPromedio.calcular_promedio_ponderado(evaluacion)
    print(f'El promedio ponderado de {evaluacion.nombre} es: {promedio:.1f}')

except ValueError as e:
    print(f'Error: {e}')