from unittest import TestCase, mock
from funcoes.banco import *


class TestBanco(TestCase):

    @mock.patch("funcoes.banco.Banco")
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_gerar_codigo_boleto_funciona(self, mock_datetime, mock_banco):
        mock_datetime.now.return_value = "0000-00-00 00:00:00.000000"
        mock_banco.codigo_banco.return_value = "180"

        dados = dict(valor=10.56)
        resultado = Banco().gerar_codigo_boleto(dados)
        self.assertEqual(resultado, "180000000000000000000001056")

        mock_datetime.now.assert_called_once()

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="123\n456"))
    @mock.patch("funcoes.banco.Banco")
    def test_testando(self, mock_banco):
        mock_banco.validar_dados_do_cartao.lines.return_value = ["A", "B"]

        self.assertEqual(Banco().validar_dados_do_cartao("1", {}), 1)

    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_credito")
    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_debito")
    def test_efetuar_pagamento(self, debito, credito):

        debito.return_value = True
        credito.return_value = True

        Banco().efetuar_pagamento("0", {})
        Banco().efetuar_pagamento("1", {})



