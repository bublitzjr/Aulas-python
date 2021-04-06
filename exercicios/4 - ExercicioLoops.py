#
# primeiraFase = [5, 9, 3, 5, 2, 1, 6, 3]
# segundaFase = []
# final = []
#
# def CalcularFase(Fase, proximaFase):
#     if (len(Fase) != 2):
#         for i in range(0, len(Fase), 2):
#             if Fase[i] != Fase[i + 1]:
#                 maior = max(Fase[i], Fase[i + 1])
#                 proximaFase.append(maior)
#             else:
#                 proximaFase.append(0)
#         return proximaFase
#     else:
#         return max(Fase[0], Fase[1])
#
# print("Primeira Fase: ", primeiraFase)
#
# print("Segunda Fase:  ", CalcularFase(primeiraFase, segundaFase))
#
# print("Final:         ", CalcularFase(segundaFase, final))
#
# print("Vencedor:      ", CalcularFase(final, 0))
#
# print("================== \n")
#
#
# # Questão 2 #
# palavras = ["Banana", "Maçã", "Pepino", "Batata"]
# print("!!!".join(palavras).upper().replace("A", "@"))
#
# # Questão 3 #
# import string
#
# alfabeto = string.ascii_lowercase
# vogais = "aeiou"
#
# palavra = input("Digite a palavra: ")
# nova_palavra = ""
#
# for i in palavra:
#     if i.lower() in vogais:
#         index = alfabeto.index(i.lower()) - 4
#         nova_palavra += alfabeto[index]
#     else:
#         index = alfabeto.index(i.lower()) + 9
#         print(index)
#         novo_index = index if index < 26 else index - 26
#         nova_palavra += alfabeto[novo_index]
#
# print(nova_palavra)
#
palavra = "bla"

