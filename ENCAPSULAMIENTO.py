class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        print("Saldo:", self.__saldo)

    def depositar(self, monto):
        self.__saldo += monto

c = Cuenta(100)
c.mostrar_saldo()
c.depositar(50)
c.mostrar_saldo()
