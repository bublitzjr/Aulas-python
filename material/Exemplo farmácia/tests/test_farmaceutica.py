from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock, mock_open
from app.farmaceutica import Farmaceutica, date


class TestFarmaceutica(TestCase):

    def test_receber_receita_works(self):
        receita = dict(nome="Clonazepan")

        far = Farmaceutica()
        retorno = far.receber_receita(receita)

        self.assertEqual(far.receita_recebida, receita)
        self.assertEqual(retorno, None)

    @patch("app.farmaceutica.date")
    def test_validar_receita_works(self, mock_date):
        mock_date.today().strftime.return_value = date(2021, 4, 26)
        mock_date.strftime.return_value = date(2022, 5, 1)

        far = Farmaceutica()
        far.receita_recebida = dict(cpf="000", validade="10")

        self.assertTrue(far.validar_receita(dict(cpf="000")))
        self.assertFalse(far.validar_receita(dict(cpf="001")))

        mock_date.today().strftime.assert_called()
        mock_date.strftime.assert_called()

    @patch("builtins.print")
    @patch("app.farmaceutica.literal_eval")
    @patch("app.farmaceutica.open", mock_open(read_data=""))
    def test_verificar_estoque_works(self, mock_literal_eval, mock_print):
        mock_literal_eval.return_value = dict(Clonazepam=dict(quantidade=10))

        far = Farmaceutica()
        far.receita_recebida = dict(quantidade_medicamento=5)

        self.assertTrue(far.verificar_estoque("Clonazepam"))
        self.assertFalse(far.verificar_estoque("Aspirina"))

        mock_literal_eval.assert_called_with("")
        mock_print.assert_called_once()
        mock_print.assert_called_with("Produto não disponível no estoque.")


    @patch("app.farmaceutica.json")
    @patch("app.farmaceutica.literal_eval")
    @patch("app.farmaceutica.open", mock_open(read_data=""))
    def test_retirar_medicamento_estoque_works(self, mock_literal_eval, mock_json):
        mock_literal_eval.return_value = dict(Clonazepam=dict(quantidade=10))

        far = Farmaceutica()
        far.receita_recebida = dict(quantidade_medicamento=5)

        mock_json.dumps.return_value = ""

        self.assertEqual(far.retirar_medicamento_estoque("Clonazepam"), None)

        mock_literal_eval.assert_called_with("")
        mock_json.dumps.assert_called_with(dict(Clonazepam=dict(quantidade=5)), indent=2)

    @patch("builtins.print")
    def test_entregar_medicamento_works(self, mock_print):

        far = Farmaceutica()
        far.receita_recebida = dict(nome="Gustavo", nome_medicamento="Conspirona")
        far.entregar_medicamento()

        mock_print.assert_called_once()
