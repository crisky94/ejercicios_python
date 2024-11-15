def crear_usuario(nombre, edad, *, ciudad, pais):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, País: {pais}")

# Llamada correcta (ciudad y país como keyword arguments)
crear_usuario("Ana", 30, ciudad="Buenos Aires", pais="Argentina")
#salida: Nombre: Ana, Edad: 30, Ciudad: Buenos Aires, País: Argentina