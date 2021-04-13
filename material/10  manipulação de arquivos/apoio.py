"""
r - read
w - write (apaga o conteúdo do arquivo e escreve)
a - append (escreve no sem apagar o que já tem no arquivo)
x - create
"""


# Abrindo e fechando um arquivo para manipulação

# file = open("teste.txt")
# file.close()
#
# # ou
#
# with open("teste.txt") as file:
#     pass


# Lendo arquivos
with open("teste.txt", "r") as file:
    file.read() # retorna o arquivo inteiro de uma vez
    # ou
    for i in file: # Percorre linha a linha
        i


# Pegando determinado número de caracteres
with open("teste.txt", "r") as file:
    file.read(5) # Retorna os primeiros 5 caracteres


# Escrevendo no arquivo apagando o conteúdo
with open("teste.txt", "w") as file:
    file.write("String")


# Escrevendo no arquivo sem apagar o conteúdo
with open("teste.txt", "a") as file:
    file.write("String")


# Deletar um arquivo
import os
os.remove("teste.txt")
