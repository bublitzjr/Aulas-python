class Prato:

    def __init__(self, recheio, preco):
        self.recheio = recheio
        self.preco = preco


class Pizza(Prato):

    def __init__(self, recheio, molho, borda, preco):
        super().__init__(recheio, preco)
        self.molho = molho
        self.borda = borda


class Salgadinho(Prato):
    def __init__(self, recheio, massa, preco):
        super().__init__(recheio, preco)
        self.massa = massa


class Lanche(Prato):

    def __init__(self, recheio, pao, molho, preco):
        super().__init__(recheio, preco)
        self.pao = pao
        self.molho = molho


class Pedido:
    def __init__(self, nomeCliente, taxaDeServico, itens: list):
        self.nomeCliente = nomeCliente
        self.taxaDeServico = taxaDeServico
        self.itens = itens

    def calcular_total(self):
        total_itens = sum([item.preco for item in self.itens])
        return total_itens + self.taxaDeServico

    def mostrar_fatura(self):
        print("------ fatura-----")
        print("Nome do cliente: " + self.nomeCliente)
        print("Taxa de Serviço: " + str(self.taxaDeServico))
        print("Preço Total: " + str(self.calcular_total()))



