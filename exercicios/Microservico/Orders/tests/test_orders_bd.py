from unittest import mock, TestCase
from Orders.DataBase.orders_bd import *

class TestOrders(TestCase):

    ################################### PERSISTIR DADOS ###############################################

    @mock.patch('Orders.DataBase.orders_bd.consultar')
    def test_persisti_dados_works(self, mock_rows):
        with mock.patch("Orders.DataBase.orders_bd.db.cursor", create=True) as mock_cursor:
            mock_cursor.execute.return_value = 1
            result = persistir_dados("")
            self.assertEqual(result, {'Status': 200, 'Text': 'Ação realizada com sucesso'})

        mock_rows.affected_rows.return_value = 0
        with self.assertRaises(Exception) as error:
            persistir_dados("")

        self.assertEqual(1065, error.exception.args[0])

    ################################### CONSULTAS ###############################################

    @mock.patch('Orders.DataBase.orders_bd.consultar')
    def test_consulta_works(self, mock_rows):

        with mock.patch("Orders.DataBase.orders_bd.db.cursor", create=True) as mock_cursor:
            mock_cursor.execute.return_value = 1

            result = consultar(1)
            self.assertEqual(result, '[]')

        mock_rows.affected_rows.return_value = 0
        with self.assertRaises(Exception) as error:
            consultar(2)

        self.assertEqual("Registro não existe", error.exception.args[0])

    ################################### CADASTRAR ###############################################

    def test_cadastra_works(self):
        dados = dict(id_user=12, item_description="kaka", item_quantity=0, item_price=0, total_value=0)
        result = cadastrar(dados)
        self.assertEqual(result, {'Status': 200, 'Text': 'Ação realizada com sucesso'})

        with self.assertRaises(Exception) as error:
            cadastrar({})

        self.assertEqual("id_user", error.exception.args[0])

    ################################### ATUALIZAR ###############################################

    def test_atualiza_works(self):
        with self.assertRaises(Exception) as error:
            dados = dict(id_user=12, item_description="flasdas", item_quantity=1, item_price=3, id=7)
            atualizar(dados)
        self.assertEqual("Não foi possível realizar a ação", error.exception.args[0])

    ################################### DELETAR ###############################################

    def test_deleta_works(self):
        with self.assertRaises(Exception) as error:
            deletar(0)
        self.assertEqual("Não foi possível realizar a ação", error.exception.args[0])

    ################################### LIMPAR ###############################################

    def test_limpa_works(self):
        with self.assertRaises(Exception) as error:
            limpar()
        self.assertEqual("Não foi possível realizar a ação", error.exception.args[0])


