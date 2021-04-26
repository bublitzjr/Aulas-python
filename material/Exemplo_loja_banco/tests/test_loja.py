from unittest import TestCase, mock
from funcoes.loja import *

class TestLoja(TestCase):

    @mock.patch("funcoes.banco.Banco")
    def test_solicitacao_pagamento_com_cartao_funciona(self, mock_banco):
        dados = dict(numero=1234, senha=3322)
        mock_banco.efetuar_pagamento.return_value = True
        result = Loja().solicitar_pagamento_com_cartao(dados, 10, "0")
        self.assertTrue(result, True)


