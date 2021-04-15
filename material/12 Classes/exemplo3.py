class Banco:

    saldo = 50000

    def __init__(self):
        # self.saldo = 50000
        pass

    def emprestar_dinheiro(self):
        Banco.saldo -= 1000
        # self.saldo -= 1000


agencia1 = Banco()
agencia2 = Banco()

agencia1.emprestar_dinheiro()

print(agencia1.saldo)
print(agencia2.saldo)
