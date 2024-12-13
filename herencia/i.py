# i. Sistema de autenticación multinivel: Crea un sistema donde los usuarios tengan roles (Admin, Editor, Viewer) y permisos diferentes para acceder a ciertos recursos. Usa métodos protegidos y privados para manejar la autenticación.
# Requisitos:

# Una clase base Usuario que maneje el login y roles.
# Subclases con métodos específicos según el rol.

class Usuario:
    def __init__(self, nombre_usuario, contraseña, rol):
        self.nombre_usuario = nombre_usuario
        self.__contraseña = contraseña
        self.__rol = rol

    def login(self, nombre_usuario, contraseña):
        if nombre_usuario == self.nombre_usuario and contraseña == self.__contraseña:
            return True
        else:
            return False
    
    def obtener_rol(self):
        return self.__rol
    
    def acceder_recurso(self, recurso):
        raise NotImplementedError('Este método debe ser implementado en las subclases')
    
class Admin(Usuario):
    def __init__(self, nombre_usuario, contraseña):
        super().__init__(nombre_usuario, contraseña, rol='Admin')

    def acceder_recurso(self, recurso):
        return f"Acceso concedido a {recurso}."
    
    def gestionar_usuarios(self):
        return 'Gestioanando usuarios...'

class Editor(Usuario):
    def __init__(self, nombre_usuario, contraseña):
                super().__init__(nombre_usuario, contraseña, rol="Editor")
    
    def acceder_recurso(self, recurso):
        if recurso in ['documento', 'imagen', 'video']:
            return f'Acceso concedido para editar {recurso}.'
        else: 
            return 'Acceso denegado a este recurso.'
    
class Viewer(Usuario):
    def __init__(self, nombre_usuario, contraseña):
        super().__init__(nombre_usuario, contraseña, rol='Viewer')

    def acceder_recurso(self, recurso):
        if recurso in ['documento', 'imagen', 'video']:
            return f'Acceso concedido para ver {recurso}'
        else:
            return 'Acceso denegado a este recurso'

    
admin = Admin(nombre_usuario='admin', contraseña='admin123')
editor = Editor(nombre_usuario='editor', contraseña='editor123')
viewer  = Viewer('viewer', 'viewer123')

if admin.login('admin', 'admin123'):
    print('Login correcto')
    print(admin.acceder_recurso('documento'))
    print(admin.gestionar_usuarios())

if editor.login('editor', 'editor123'):
    print('\nLogin correcto')
    print(editor.acceder_recurso('documento'))
    print(editor.acceder_recurso('audio'))

if viewer.login('viewer', 'viewer123'):
    print('\nLogin correcto')
    print(viewer.acceder_recurso('documento'))
    print(viewer.acceder_recurso('video'))