from datetime import date

class Cadastro:

    def teste(self):
        return date.today() <= date(2021, 4, 26)

    def printar(self, testea):
        print(self.cursor)

    def cadastrar(self, usuario):

        email = usuario.email
        senha = usuario.senha

        return email, senha
