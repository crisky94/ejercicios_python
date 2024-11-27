# a. Sistema de notificaciones: Crea una clase base Notificacion con un método enviar. Implementa subclases como Email, SMS y PushNotification.
class Notificacion:
    def __init__(self, notificacion):
        self.notificacion = notificacion
    
    def enviar(self, notificacion):
        if not self.notificacion:
            print('No hay notificaciones')
        return (f'Notificacion: {self.notificacion} enviada')

class Email(Notificacion):

    def __init__(self, notificacion):
        # Llamar al constructor de la clase base
        super().__init__(notificacion)

    def enviar(self):
        return f'Enviando email: {self.notificacion}'

class SMS(Notificacion):

    def __init__(self, notificacion):
        # Llamar al constructor de la clase base
        super().__init__(notificacion)

    def enviar(self):
        return f'Enviando sms: {self.notificacion}'

class PushNotification(Notificacion):
    
    def __init__(self, notificacion):
        # Llamar al constructor de la clase base
        super().__init__(notificacion)

    def enviar(self):
        return f'Enviando pushNotification: {self.notificacion}'

email = Email('Hola email')
sms = SMS('Hola SMS')
pushNotification = PushNotification('Hola pushNotification')


print(email.enviar())
print(sms.enviar())
print(pushNotification.enviar())

