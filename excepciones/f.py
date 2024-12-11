# f. Búsqueda en diccionario
# Crea una función buscar_clave(diccionario, clave) que maneje la ausencia de una clave en un diccionario.

def buscar_clave(diccionario, clave):
    
        if not clave in diccionario:
            raise ValueError(f'La clave {clave} no se ha encontrado')
        else:
            return clave
        
try:
    diccionario =  {"nombre": "Kenay", "apellido": "Labrador"}
    clave = input('Introduce la clave que quieres buscar: ')
    buscar_clave(diccionario, clave)
    print(f'La clave {clave} ha sido encontrada')
except ValueError as e:
    print(f'Error: {e}')
