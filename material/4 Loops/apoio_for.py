# Criação do for
"""
for variavel_de_escopo in iterável:
    comandos...
"""

# Usando uma lista como iterável
lista1 = ["A", "B", "C"]
for var in lista1:
    var # retorna "A", depois "B", depois "C"


# Usando um range() como iterável
for var in range(5):
    var # retorna 0, depois 1, depois 2, depois 3, depois 4


# range() também é muito usando com a função len(), para ser executado um número de vezes indeterminadas
lista1 = ["A", "B", "C"]
for var in range(len(lista1)):
    var # retorna 0, depois 1, depois 2
    lista1[var] # retorna "A", depois "B", depois "C"
# Nesse caso, var está sendo usado para acessar uma posição de lista


# Usando 'else' no for
# A cláusula 'else' será ativada após o loop 'for' acabar, exceto se acabar forçadamente por um 'break'
for i in range(99):
    i
else:
    print("Aqui")

# Caso o 'for' não tenha nada para percorrer, ele irá direto ao 'else'
for i in range(0):
    i # O programa não chega até essa linha, pois não há nada para o 'for' percorrer
else:
    print("Aqui")


# 'For' em uma linha (Comprehensive For)
"""
lista = [var for var in iterável]

equivale a:

lista = []
for var in iteravel:
    lista.append(var)    

"""

# Esse tipo de for, é comumente usado dentro de listas [] e sets {}
x = [i for i in range(5)] # x é igual a [0, 1, 2, 3, 4]

lista1 = ["A", "B", "C"]
x = ["Letra: " + i for i in lista1] # x é igual a ["Letra: A", "Letra: B", "Letra:  C"]


# Usando 'for' de uma linha com condição
"""
lista = [var for var in iterável if condição]

equivale a:

lista = []
for var in iteravel:
    if condição:
        lista.append(var)   
"""

x = [i for i in range(10) if i % 2 == 0] # Verifica se 'i' é um número par, e só adiciona à lista os que forem
# x é igual a [0, 2, 4, 5, 6, 8


# Usando 'continue'
for i in range(10):
    if i % 2 == 0:
        continue
    else:
        print("Ímpar")
# 'continue' faz com que o resto do loop 'for' seja ignorado


# Usando 'pass'
for i in range(10):
    pass
# 'pass' só passará sem fazer nada

# 'pass' geralmente é usado quando não sabemos ainda o que queremos fazer dentro de algo


# Usando 'break'
for i in range(10):
    if i >= 5:
        break # Quebra o loop quando i for maior ou igual a 5
# 'break' é usado para quebrar o loop que estiver superior a ele
