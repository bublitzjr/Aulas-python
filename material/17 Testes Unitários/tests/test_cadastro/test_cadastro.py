from unittest import mock, TestCase
# from ..app.cadastro.main_cadastro import Cadastro

class TestCadastro(TestCase):

    def test_cadastrar(self):
        usuario = mock.MagicMock()
        usuario.email = "aa@gmail.com"
        usuario.senha = "sorvete"

        email, senha = Cadastro().cadastrar(usuario)
        self.assertEqual(email, "aa@gmail.com")
        self.assertEqual(senha, "sorvete")

    @mock.patch("app.cadastro.main_cadastro.date")
    def test_teste(self, mock_date):
        mock_date.today().__le__.return_value = True
        
        self.assertTrue(Cadastro().teste())
        
        
print(__name__)