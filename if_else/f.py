# f. Verificar acceso según el rol de usuario
# Solicita al usuario que ingrese su rol en una plataforma (administrador, editor o visitante) y muestra un mensaje con los permisos correspondientes:

# Administrador: “Tienes acceso total.”
# Editor: “Tienes acceso limitado para editar.”
# Visitante: “Tienes acceso de solo lectura.”

rol = input('Ingresa tu rol: ').lower()

mensaje = ''

if rol == 'administrador':
    mensaje = 'Tienes acceso total'
elif rol == 'editor':
    mensaje = 'Acceso limitado'
else:
    mensaje = 'Acceso RO'

print(f'Tu rol {rol} , {mensaje}')