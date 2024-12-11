# b. Validación de edad
# Crea una función verificar_edad(edad) que lance una excepción si la edad es negativa.


# def verificar_edad(edad):
#     if edad > 0:
#         return edad
#     else:
#         raise ValueError('La edad no puede ser negativa, ni zero')


# edad = int(input('Introduce tu edad: '))
# verificar_edad(edad)

def verificar_edad(edad):
    
    if edad < 0:
        raise ValueError('Tu edad no puede ser zero ni negativa')
    
try:
    edad = int(input('Escribe tu edad: '))
    verificar_edad(edad)
except ValueError as e :
    print(f'Error: {e}')