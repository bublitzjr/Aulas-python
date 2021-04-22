from builtins import print
from unittest import TestCase, mock
from funcoes.banco import *
from datetime import date

class TestBanco(TestCase):

    @mock.patch("datetime.datetime")
    @mock.patch("funcoes.banco.Banco")
    def test_gerar_codigo_boleto_funciona(self, mock_codigo_banco, mock_date_time):
        mock_codigo_banco.codigo_banco.return_value = 180
        mock_date_time.now.return_value = "0000000000000000000000000"
        dados = dict(valor=10)
        result = Banco().gerar_codigo_boleto(dados)
        self.assertEqual(result, "180000000000000000000000000010")

    def test_gerar_boleto_funciona(self):
        dados = dict(valor=20, data=1010, codigo="123", conta_loja="213")
        dado_esperado = {'valor': 20, 'data_validade': 1013, 'código': '18012320', 'conta_recebedora': '213'}
        result = Banco().gerar_boleto(dados)

        self.assertDictEqual(result, dado_esperado)

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="123;123;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.Banco.validar_dados_do_cartao")
    def test_efetuar_pagamento_cartao_debito_funciona(self, mock_dados_cartao):
        dados = dict(numero="123", senha="123", valor_compra=10)
        mock_dados_cartao.return_value = True
        result = Banco().efetuar_pagamento_com_cartao_debito(dados)
        self.assertTrue(result)

        mock_dados_cartao.return_value = False
        result = Banco().efetuar_pagamento_com_cartao_debito(dados)
        self.assertFalse(result)

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="123;123;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.Banco.validar_dados_do_cartao")
    def test_efetuar_pagamento_cartao_credito_funciona(self, mock_dados_cartao):
        dados = dict(numero="123", senha="123", valor_compra=10)
        mock_dados_cartao.return_value = True
        result = Banco().efetuar_pagamento_com_cartao_credito(dados)
        self.assertTrue(result)

        mock_dados_cartao.return_value = False
        result = Banco().efetuar_pagamento_com_cartao_credito(dados)
        self.assertFalse(result)

    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_credito")
    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_debito")
    def test_efetuar_pagamento_funciona(self, debito, credito):
        debito.return_value = True
        credito.return_value = True

        Banco().efetuar_pagamento("0", {})
        Banco().efetuar_pagamento("1", {})

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="0;0;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_validar_dados_do_cartao_funciona(self, mock_datetime):
        mock_datetime.today.return_value = date(2021, 4, 1)
        mock_datetime.strptime.return_value = date(2024, 10, 1)
        resultado = Banco().validar_dados_do_cartao("0", {"numero": "0", "senha": "0", "valor_compra": 0.0})
        self.assertTrue(resultado)
        self.assertFalse(not resultado)

        mock_datetime.today.assert_called_once()




