# i. Operación en archivo
# Escribe una función leer_archivo(nombre_archivo) que maneje errores al intentar abrir un archivo inexistente.


def leer_archivo(nombre_archivo):
    if not nombre_archivo:
        raise ValueError('Debe proporcionar un nombre de archivo válido.')
    
#El modo 'r' significa que estamos abriendo el archivo en modo de solo lectura.
#El uso de with asegura que el archivo se cierre automáticamente después de ser leído, incluso si ocurre un error.
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
    except FileExistsError:
        print(f'Error: El archivo {nombre_archivo} no exite')

#IOError = problema general relacionado con operaciones de entrada/salida, como leer o escribir archivos.
    except IOError as e:
        print(f'Error al intentar abirir el archivo: {e}')