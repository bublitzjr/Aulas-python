# [9, 2, 2, 1, 5]
#  0  1  2  3  4 --- Posições

#  [9, 2, 2, 1, 5]
#  -5 -4 -3 -2 -1 --- Posições

# Criação de lista
lista = []
# ou
lista = list()


# len retona o tamanho da lista
len([0, 1, 1, 2]) # retorna 4


# Acessando um index só
["a", "b", "c"][1] # retorna "b"
[1, True, "3", 4, 5][-2] # retorn 4


# Acessando por vários indexes
["Teste", "Ana", 2, 1, 3][0:3] # retorna ["Teste", "Ana", 2]
[1, 2, 3, 4, 5][0:] # retorna [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5][:4] # retorna Test [1, 2, 3, 4]
["A", "B", "C"][:] # retorna ["A", "B", "C"]
[1, 2, 3, 4, 5][-5:-2] # retorna [1, 2, 3]

# Usando o passo
[1, 2, 3, 4, 5][::2] # retorna [1, 3, 5]
[1, 2, 3, 4, 5][1:4:2] # retorna [2, 4]
["A", "B", "C"][::-1] # retorna ["C", "B", "A"]


# Atribuindo um valor à uma posição
lista = [1, 2, 3, 4]
lista[3] = "A" # lista se torna [1, 2, 3, "A"]


# Atribuindo valores à várias posições
lista = [1, 2, 3, 4]
lista[0:2] = ["AB"] # lista se torna ["AB", 3, 4]

lista = [1, 2, 3, 4]
lista[0:2] = ["AB", True] # lista se torna ["AB", True, 3, 4]

lista = [1, 2, 3, 4]
lista[0:2] = ["AB", True, 2] # lista se torna ['AB', True, 2, 3, 4]


# insert() inclui um valor em uma posição escolhida
lista = [1, 2, 3, 4]
lista.insert(2, "A") # lista se torna [1, 2, "A", 3, 4]


# append() adiciona um item no final da lista
lista = [1, 2, 3, 4]
lista.append(5) # lista se torna [1, 2, 3, 4, 5]


# extend() extende a lista
lista = [1, 2, 3, 4]
lista2 = ["A", "B", "C"]
lista.extend(lista2) # lista se torna [1, 2, 3, 4, "A", "B", "C"]


# usar o sinal + entre duas listas ou mais listas as une
lista = [1, 2, 3, 4]
lista2 = ["A", "B", "C"]
lista = lista + lista2 # lista se torna [1, 2, 3, 4, "A", "B", "C"]


# remove() retira um valor da lista
lista = [1, 2, 3, 4]
lista.remove(2) # lista se torna [1, 3, 4]

lista2 = ["A", "B", "C"]
lista2.remove("C") # lista se torna ["A", "B"]


# pop() remove um valor através de uma posição
lista = [1, 2, 3, 4]
lista.pop(2) # lista se torna [1, 2, 4]

# se não for passado argumento, pop() removerá a última posição
lista2 = ["A", "B", "C"]
lista2.pop() # lista se torna ["A", "B"]


# clear() deixa a lista vazia
lista = [1, 2, 3, 4]
lista.clear() # lista se torna []


# sort() ordena a lista em posição crescente
lista = [4, 2, 1, 3]
lista.sort() # lista se torna [1, 2, 3, 4]

# se passado o argumento reverse=True, a lista ficará em ordem decrescente
lista2 = ["A", "B", "C"]
lista2.sort(reverse=True)


# reverse() faz com que a lista fique ao contrário (não em ordem decrescente)
lista = [2, 1, 5, 4]
lista.reverse() # lista se torna [4, 5, 1, 2]


# copy() retorna uma cópia da lista
lista = [1, 2, 3, 4]
lista2 = lista.copy() # retorna [1, 2, 3, 4]


# join() junta todos os elementos de uma lista em uma string (porém todos os elementos da lista devem ser strings)
lista = [1, 2, 3, 4]
"".join(lista) # retorna um erro

lista2 = ["A", "B", "C"]
"".join(lista2) # retorna "ABC"

lista3 = ["A", "B", "C"]
"--".join(lista2) # retorna "A--B--C"

lista4 = ["1", "2", "3"]
"Pewpew".join(lista2) # retorna "1Pewpew2Pewpew3"
