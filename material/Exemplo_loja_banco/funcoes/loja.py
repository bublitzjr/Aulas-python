from funcoes.banco import Banco

class Loja:

    def __init__(self):
        self.caixa = 50000
        self.conta_loja = "000124578"

    def solicitar_pagamento_com_cartao(self, dados_cartao: dict, valor_compra: float, modalidade_pagamento: str):
        dados_requisicao = dict(numero=dados_cartao["numero"],
                                senha=dados_cartao["senha"],
                                valor_compra=valor_compra)
        resultado = Banco().efetuar_pagamento(modalidade_pagamento, dados_requisicao)

        if resultado:
            self.caixa += valor_compra
            return "Compra efetuada com sucesso!"
        else:
            return "Compra efetuada com fracasso!"


    def solicitar_boleto(self, dados_compra: dict):
        dados_requisicao = dict(conta_loja=self.conta_loja,
                                valor=dados_compra["valor"],
                                data=dados_compra["data"])

        boleto = Banco().gerar_boleto(dados_requisicao)
        return boleto

    def efetuar_pagamento_com_dinheiro(self, dinheiro, valor_compra):
        if dinheiro >= valor_compra:
            troco = dinheiro - valor_compra
            self.caixa += valor_compra
            return troco
        else:
            return "Tente novamente mais tarde!"

# teste = Loja()
# teste.solicitar_boleto(dict(conta_loja="234", valor=10, data=1010))