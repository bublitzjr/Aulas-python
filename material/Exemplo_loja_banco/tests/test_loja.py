from unittest import TestCase, mock
from funcoes.loja import *


class TestLoja(TestCase):

    @mock.patch("funcoes.banco.Banco.efetuar_pagamento")
    def test_solicitacao_pagamento_com_cartao_funciona(self, mock_pagamento):
        dados = dict(numero=1234, senha=3322)

        mock_pagamento.return_value = True
        result = Loja().solicitar_pagamento_com_cartao(dados, 10, "0")
        self.assertEqual(result, "Compra efetuada com sucesso!")

        mock_pagamento.return_value = False
        result = Loja().solicitar_pagamento_com_cartao(dados, 10, "1")
        self.assertEqual(result, "Compra efetuada com fracasso!")

    def test_solicitar_boleto(self):
        dados = dict(conta_loja="234", valor=10, data=1010)
        dados_esperados = {'valor': 10, 'data_validade': 1013, 'código': '18012310', 'conta_recebedora': '000124578'}

        result = Loja().solicitar_boleto(dados)
        self.assertDictEqual(result, dados_esperados)

    def test_efetuar_pagamento_com_dinheiro(self):
        result = Loja().efetuar_pagamento_com_dinheiro(20, 10)
        self.assertEqual(result, 10)

        result = Loja().efetuar_pagamento_com_dinheiro(20, 30)
        self.assertEqual(result, "Tente novamente mais tarde!")