from unittest import mock, TestCase
from Users.DataBase.usuarios_bd import *

class TestUser(TestCase):

    ################################### PERSISTIR DADOS ###############################################

    @mock.patch('Users.DataBase.usuarios_bd.consultar')
    def test_persisti_dados_works(self, mock_rows):
        with mock.patch("Users.DataBase.usuarios_bd.db.cursor", create=True) as mock_cursor:
            mock_cursor.execute.return_value = 1
            result = persistir_dados("")
            self.assertEqual(result, {'Status': 200, 'Text': 'Ação realizada com sucesso'})

        mock_rows.affected_rows.return_value = 0
        with self.assertRaises(Exception) as error:
            persistir_dados("")

        self.assertEqual(1065, error.exception.args[0])

    ################################### CONSULTAS ###############################################

    @mock.patch('Users.DataBase.usuarios_bd.consultar')
    def test_consulta_works(self, mock_rows):

        with mock.patch("Users.DataBase.usuarios_bd.db.cursor", create=True) as mock_cursor:
            mock_cursor.execute.return_value = 1
            result = consultar("123")

            self.assertEqual(result, '[]')

        mock_rows.affected_rows.return_value = 0
        with self.assertRaises(Exception) as error:
            consultar("4124124124124")

        self.assertEqual("Usuário não existe", error.exception.args[0])

    ################################### CADASTRAR ###############################################

    def test_cadastra_works(self):
        dados = dict(Name="Jeff", CPF="4124343", Email="avx", Phone_number="123")
        result = cadastrar(dados)
        self.assertEqual(result, {'Status': 200, 'Text': 'Ação realizada com sucesso'})

        with self.assertRaises(Exception) as error:
            cadastrar({})

        self.assertEqual("Name", error.exception.args[0])

    ################################### ATUALIZAR ###############################################

    def test_atualiza_works(self):
        with self.assertRaises(Exception) as error:
            dados = dict(Name="Jeff", CPF="3123", Email="avx", Phone_number="123")
            atualizar(dados)
        self.assertEqual("Não foi possível realizar a ação", error.exception.args[0])

    ################################### DELETAR ###############################################

    def test_deleta_works(self):
        with self.assertRaises(Exception) as error:
            deletar("123")
        self.assertEqual("'int' object is not subscriptable", error.exception.args[0])

    ################################### LIMPAR ###############################################

    def test_limpa_works(self):
        with self.assertRaises(Exception) as error:
            limpar()
        self.assertEqual(1451, error.exception.args[0])

