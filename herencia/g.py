#### g. **Sistema de pagos avanzado:** Crea subclases de `MetodoDePago` con validaciones privadas para asegurarte de que los datos del usuario sean correctos.
import re

class MetodoDePago:
    def __init__(self, metodo, moneda, activo = True):
        self.metodo = metodo
        self.moneda = moneda
        self.activo = activo

    def procesar_pago(self, cantidad):
        if not self.activo:
            raise ValueError(f'El método {self.metodo} esta inactivo.')
        print(f'Procesando pago de cantidad {cantidad} {self.moneda} con {self.metodo}...')
    

    def mostrar_info(self):
        return f"Método: {self.metodo}, Moneda: {self.moneda}, Activo: {self.activo}"
    
    def validar(self):
        raise NotImplementedError('El método de validación debe implementarse en la subclase')
    
class TarjetaCredito(MetodoDePago):
    def __init__(self, numero_tarjeta, fecha_expiracion, cvv, metodo='Tarjeta de Crédito', moneda='USD', activo=True):
        super().__init__(metodo, moneda, activo)
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv

    def __validar_numero_tarjeta(self):
        if len(self.numero_tarjeta) != 16 or not self.numero_tarjeta.isdigit():
            raise ValueError('El número de la tarjeta debe tener 16 dígitos y ser númerico.')
        
    def __validar_fecha_expiracion(self):
        if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", self.fecha_expiracion):
            raise ValueError('La fecha de expiración debe tener el formato MM//AA.')
        
    def __validar_cvv(self):
        if len(self.cvv) != 3 or not self.cvv.isdigit():
            raise ValueError('El CVV debe contener 3 dígitos númericos.')
        
    def validar(self):
        self.__validar_numero_tarjeta()
        self.__validar_fecha_expiracion()
        self.__validar_cvv()

    def procesar_pago(self, cantidad):
        self.validar()
        super().procesar_pago(cantidad)
        print(f"Pago procesado con tarjeta terminada en {self.numero_tarjeta[-4:]}.")

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tarjeta: {self.numero_tarjeta[-4:]}"
    
class Paypal(MetodoDePago):
    def __init__(self, correo_electronico, metodo='PayPal', moneda='USD', activo=True ):
        super().__init__(metodo, moneda, activo)
        self.correo_electronico = correo_electronico
    
    def __validar_correo(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo_electronico):
            raise ValueError('El correo electrónico no es válido.')
    
    def validar(self):
        self.__validar_correo()

    def procesar_pago(self, cantidad):
        self.validar()
        super().procesar_pago(cantidad)
        print(f"Pago procesando a través de PayPal con la cuenta  {self.correo_electronico}")
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Correo: {self.correo_electronico}"
    
try:
    tarjeta = TarjetaCredito(numero_tarjeta="1234567812345678", fecha_expiracion="12/25", cvv="123")
    tarjeta.procesar_pago(100)
    print(tarjeta.mostrar_info())
    paypal = Paypal(correo_electronico='usuario@gmail.com')
    paypal.procesar_pago(50)
    print(tarjeta.mostrar_info())
except ValueError as e :
    print(f'Error: {e}')
