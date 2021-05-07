from unittest import mock, TestCase
from Orders.controllers.orders import *

class TestUsuario(TestCase):

    ################################### CONSULTAR ###############################################

    @mock.patch('Orders.controllers.orders.orders_bd.consultar')
    def test_lista_works(self, mock_consultar):
        mock_consultar.return_value = ""

        result = listar_pedidos("")
        self.assertEqual(result, "")

        delattr(orders_bd, "consultar") # Deletando atributo da classe
        result = listar_pedidos("")
        expected = {'Status': 400, 'Text': "module 'Orders.DataBase.orders_bd' has no attribute 'consultar'"}
        self.assertEqual(result, expected)

    ################################### CADASTRAR ###############################################

    @mock.patch('Orders.controllers.orders.orders_bd.cadastrar')
    def test_cadastra_works(self, mock_cadastrar):
        mock_cadastrar.return_value = ""

        result = cadastrar_pedidos("")
        self.assertEqual(result, "")

        delattr(orders_bd, "cadastrar") # Deletando atributo da classe
        result = cadastrar_pedidos("")
        expected = {'Status': 400, 'Text': "module 'Orders.DataBase.orders_bd' has no attribute 'cadastrar'"}
        self.assertEqual(result, expected)

    ################################### ATUALIZAR ###############################################

    @mock.patch('Orders.controllers.orders.orders_bd.atualizar')
    def test_atualiza_works(self, mock_atualizar):
        mock_atualizar.return_value = ""

        result = atualizar_pedidos("")
        self.assertEqual(result, "")

        delattr(orders_bd, "atualizar") # Deletando atributo da classe
        result = atualizar_pedidos("")
        expected = {'Status': 400, 'Text': "module 'Orders.DataBase.orders_bd' has no attribute 'atualizar'"}
        self.assertEqual(result, expected)

    ################################### DELETAR ###############################################

    @mock.patch('Orders.controllers.orders.orders_bd.deletar')
    def test_deleta_works(self, mock_deletar):
        mock_deletar.return_value = ""

        result = deletar_pedidos("")
        self.assertEqual(result, "")

        delattr(orders_bd, "deletar") # Deletando atributo da classe
        result = deletar_pedidos("")
        expected = {'Status': 400, 'Text': "module 'Orders.DataBase.orders_bd' has no attribute 'deletar'"}
        self.assertEqual(result, expected)

    ################################### LIMPAR ###############################################

    @mock.patch('Orders.controllers.orders.orders_bd.limpar')
    def test_limpa_works(self, mock_limpar):
        mock_limpar.return_value = ""

        result = limpar_pedidos()
        self.assertEqual(result, "")

        delattr(orders_bd, "limpar") # Deletando atributo da classe
        result = limpar_pedidos()
        expected = {'Status': 400, 'Text': "module 'Orders.DataBase.orders_bd' has no attribute 'limpar'"}
        self.assertEqual(result, expected)