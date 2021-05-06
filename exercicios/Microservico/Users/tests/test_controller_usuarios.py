from unittest import mock, TestCase
from Users.controllers.usuarios import *

class TestUsuario(TestCase):

    ################################### CONSULTAR ###############################################

    @mock.patch('Users.controllers.usuarios.usuarios_bd.consultar')
    def test_lista_works(self, mock_consultar):
        mock_consultar.return_value = ""

        result = listar_usuario("")
        self.assertEqual(result, "")

        delattr(usuarios_bd, "consultar") # Deletando atributo da classe
        result = listar_usuario("")
        expected = {'Status': 400, 'Text': "module 'Users.DataBase.usuarios_bd' has no attribute 'consultar'"}
        self.assertEqual(result, expected)

    ################################### CADASTRAR ###############################################

    @mock.patch('Users.controllers.usuarios.usuarios_bd.cadastrar')
    def test_cadastra_works(self, mock_cadastrar):
        mock_cadastrar.return_value = ""

        result = cadastrar_usuarios("")
        self.assertEqual(result, "")

        delattr(usuarios_bd, "cadastrar") # Deletando atributo da classe
        result = cadastrar_usuarios("")
        expected = {'Status': 400, 'Text': "module 'Users.DataBase.usuarios_bd' has no attribute 'cadastrar'"}
        self.assertEqual(result, expected)

    ################################### ATUALIZAR ###############################################

    @mock.patch('Users.controllers.usuarios.usuarios_bd.atualizar')
    def test_atualiza_works(self, mock_atualizar):
        mock_atualizar.return_value = ""

        result = atualizar_usuarios("")
        self.assertEqual(result, "")

        delattr(usuarios_bd, "atualizar") # Deletando atributo da classe
        result = atualizar_usuarios("")
        expected = {'Status': 400, 'Text': "module 'Users.DataBase.usuarios_bd' has no attribute 'atualizar'"}
        self.assertEqual(result, expected)
        
    ################################### DELETAR ###############################################

    @mock.patch('Users.controllers.usuarios.usuarios_bd.deletar')
    def test_deleta_works(self, mock_deletar):
        mock_deletar.return_value = ""

        result = deletar_usuarios("")
        self.assertEqual(result, "")

        delattr(usuarios_bd, "deletar") # Deletando atributo da classe
        result = deletar_usuarios("")
        expected = {'Status': 400, 'Text': "module 'Users.DataBase.usuarios_bd' has no attribute 'deletar'"}
        self.assertEqual(result, expected)

    ################################### LIMPAR ###############################################

    @mock.patch('Users.controllers.usuarios.usuarios_bd.limpar')
    def test_limpa_works(self, mock_limpar):
        mock_limpar.return_value = ""

        result = limpar_usuarios()
        self.assertEqual(result, "")

        delattr(usuarios_bd, "limpar") # Deletando atributo da classe
        result = limpar_usuarios()
        expected = {'Status': 400, 'Text': "module 'Users.DataBase.usuarios_bd' has no attribute 'limpar'"}
        self.assertEqual(result, expected)

    
    