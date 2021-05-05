from unittest import TestCase
from app.paciente import Paciente


class TestPaciente(TestCase):

    def test_init_works(self):
        documento = dict(nome="Gustavo", cpf="000")
        receita = dict(nome="Gustavo", cpf="000",
                       nome_medicamento="Asperina",
                       quantidade_medicamento=5, validade="02/05/2002")

        pac = Paciente(documento, receita)

        self.assertEqual(pac.nome, "Gustavo")
        self.assertEqual(pac.cpf, "000")
        self.assertEqual(pac.documento, documento)
        self.assertEqual(pac.receita, receita)
