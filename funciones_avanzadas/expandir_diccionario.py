def mostrar_detalles(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

#mostrar_detalles(datos['nombre'], datos['edad'], datos['ciudad'])
mostrar_detalles(nombre=datos['nombre'], edad=datos['edad'], ciudad=datos['ciudad'])
datos = {"nombre": "Juan", "edad": 30, "ciudad": "La Plata"}
mostrar_detalles(**datos)