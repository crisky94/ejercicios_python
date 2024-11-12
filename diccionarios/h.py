# h. Diccionario de traducciones
# Crea un diccionario donde las claves sean palabras en español y los valores sean sus traducciones en inglés. Luego, permite al usuario ingresar una palabra en español y muestra su traducción. Si la palabra no está en el diccionario, muestra un mensaje indicando que la palabra no tiene traducción.

traducciones = {'perro': 'dog', 'gato': 'cat', 'casa': 'house'}
palabra =  input('Ingresa una palabra en español para traducirla al inglés: ')

if palabra in traducciones:
        print(traducciones[palabra])
else:
        print('La palabra no tiene traducción')
# Salida esperada: La traducción de 'gato' es 'cat'.