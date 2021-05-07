from unittest import mock, TestCase
from Users.security.criptografia import *

class TestUsuario(TestCase):

        @mock.patch('Users.security.criptografia.codificar_dado')
        def test_codificar_dado_works(self, mock_codificar_dado):
            mock_codificar_dado.dado_codificado.return_value = ""

            result = codificar_dado("")
            self.assertEqual(result, "")

        @mock.patch('Users.security.criptografia.decodificar_dado')
        def test_decodificar_dado_works(self, mock_decodificar_dado):
            mock_decodificar_dado.dado_decodificado.return_value = ""

            result = decodificar_dado("")
            self.assertEqual(result, "")

