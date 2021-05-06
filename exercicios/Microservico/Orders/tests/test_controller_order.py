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
    