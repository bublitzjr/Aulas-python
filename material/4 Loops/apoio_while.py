# Criação do 'while'

"""
while condição:
    comandos...
"""

contador = 1
while contador < 10:
    contador += 1

print(contador) # Retorna 10


# Cirando um while infinito
contador = 0
while True:
    if contador > 10:
        break # Quebra o loop quando i for maior que 10
    contador += 1
# 'break' é usado para quebrar o loop que estiver superior a ele


# Usando 'else' no 'while'
# A cláusula 'else' será ativada caso a condição do while não seja mais verdadeira
contador = 0
while contador <= 5:
    contador += 1
else:
    contador # Retorna 6


# Usando 'continue'
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    else:
        print("Ímpar")
# 'continue' faz com que o resto do loop 'while' seja ignorado
