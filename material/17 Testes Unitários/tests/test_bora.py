from unittest import TestCase, mock
from app.bora import *


class TestandoBora(TestCase):

    def test_soma_is_working(self):
        n1 = 10
        n2 = 12
        self.assertEqual(soma(n1, n2), 22)

    def test_raiz_ta_funfando(self):

        type_test = "A"
        with self.assertRaises(TypeError):
            raiz(type_test)

        value_test = -9
        with self.assertRaises(ValueError):
            raiz(value_test)

        self.assertEqual(raiz(144), 12)

    def test_lista(self):
        self.assertTrue(listadef(0))
        self.assertFalse(listadef(1))

    # @mock.patch("app.bora.randint", return_value=2)
    # def test_muitas_strings_works(self, mock_rand):
    #     self.assertEqual(muitas_strings("ABC"), "")

    @mock.patch("app.bora.listadef")
    @mock.patch("app.bora.randint")
    def test_muitas_strings_works(self, mock_rand, mock_listadef):
        mock_rand.return_value = 2
        self.assertEqual(muitas_strings("ABC"), "ABCABC")

        mock_rand.assert_has_calls([mock.call(1, 2), mock.call(1, 100)])
