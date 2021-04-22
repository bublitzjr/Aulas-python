# class Error(Exception):
#     pass


# class SalarioAbaixoDoEsperado(Error):
#
#     def __init__(self, salario):
#         if salario < 2000:
#             restante = 2000 - salario
#             mensagem = "Seu salário está diferente do esperado!\n" \
#                        f"Ainda faltam R${restante}"
#             super().__init__(mensagem, mensagem)


# class Verifica(Error):
#
#     def __init__(self, altura=None, idade=None):
#         nao_declaradas = []
#         if not idade:
#             nao_declaradas.append("Idade não foi declarada!")
#         if not altura:
#             nao_declaradas.append("Altura não foi declarada!")
#
#         super().__init__(nao_declaradas)

# try:
#     # raise SalarioAbaixoDoEsperado(1000)
#     raise Verifica(1.8, 100)
# except Exception as error:
#     print(error.args)

# raise Verifica(altura=10)


# try:
#     raise Exception("A", "B")
# except Exception as error:
#     print("Seu erro foi:", error.args)


