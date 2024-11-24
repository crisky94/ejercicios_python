# a. Crea una clase Cuenta que permita depositar y retirar dinero.
class Cuenta:
    def __init__(self, saldo_inicial: float) -> None:
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, monto: float) -> None:
        self.saldo_inicial += monto
    
    def retirar(self, monto: float) -> None:
        if self.saldo_inicial < monto:
            raise ValueError("Saldo insuficiente")
        self.saldo_inicial -= monto
cuenta = Cuenta(10000)
cuenta.depositar(5000)
cuenta.retirar(2000)
print(cuenta.saldo_inicial)