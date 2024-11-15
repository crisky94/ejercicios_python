def procesar(param1, param2, param3, nombre=None, edad=None):
    print(f"{param1=}, {param2=}, {param3=}")
    print(f"Nombre: {nombre}, Edad: {edad}")

lista = ['a', 'b', 'c']
dicc = {"nombre": "Pedro", "edad": 45}

procesar(*lista, **dicc)

# salida :
# param1='a', param2='b', param3='c'
# Nombre: Pedro, Edad: 45