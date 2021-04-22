import unittest
from funcoes.bora import *

class TestBora(unittest.TestCase):

    def test_soma_funciona(self):
        n1 = 10
        n2 = 20
        self.assertEqual(soma(n1, n2), 30)

    def test_raiz_funciona(self):

        type_test = "A"
        with self.assertRaises(TypeError): # Erros com raise Exception
            raiz(type_test)

        value_test = -9
        with self.assertRaises(ValueError):  # Erros com raise Exception
            raiz(value_test)

        self.assertEqual(raiz(144), 12)