# class Funcionarios:
#
#     TEMPO_MAXIMO_VIAGEM = 14
#
#     salario: int
#     local_de_trabalho: str
#     ferias_acumuladas: float
#     codigo: int
#     saldo_para_viagem: float
#
#     def pedir_ferias(self, pedido):
#         resultado = True if pedido <= self.ferias_acumuladas else False
#         if resultado: self.ferias_acumuladas -= pedido
#         return resultado
#
#     def bater_ponto(self, hora_batida_inicial, hora_batida_final):
#         tempo_de_trabalho = hora_batida_final - hora_batida_inicial
#         if tempo_de_trabalho < 8:
#             return "Ainda falta tempo"
#         return "Até amanhã"
#
#     def agendar_viagem(self, data_inicial, data_final, orcamento):
#
#         if orcamento > self.saldo_para_viagem:
#             return False
#         tempo_viagem = data_final - data_inicial
#         if tempo_viagem > self.TEMPO_MAXIMO_VIAGEM:
#             return False
#         return True
#
#
# class Gerente(Funcionarios):
#
#     def __init__(self, salario, local_de_trabalho, ferias_acumuladas,
#                  codigo, saldo_para_viagem):
#         self.salario = salario
#         self.local_de_trabalho = local_de_trabalho
#         self.ferias_acumuladas = ferias_acumuladas
#         self.codigo = codigo
#         self.saldo_para_viagem = saldo_para_viagem
#
#
# pessoa1 = Gerente(10000, "Bluemanu", 12, "3545", 3000)
# print(pessoa1.salario)
# print(pessoa1.ferias_acumuladas)
# print(pessoa1.pedir_ferias(10))
# print(pessoa1.bater_ponto(8, 15))
# 
# class Mae:
# 
#     def __init__(self):
#         print("Classe Mãe")
# 
# 
# class Filha(Mae):
# 
#     def __init__(self):
#         super().__init__()
#         print("Classe Filha")
# 
# 
# fil = Filha()
