class CuentaBancaria:
    def __init__(self, titular, saldo, tipo_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        elif cantidad > 0:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def mostrar_saldo(self):
        print(f"Saldo actual de la cuenta: {self.saldo}")


cuenta = CuentaBancaria("Alejandro Martín", 1000, "ahorros")
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.retirar(1500)  
