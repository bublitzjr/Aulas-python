# Criação de tuplas
"""
tupla = ()
ou
tupla = tuple()
"""
tupla = (1, 2, 3)

# Criar tupla com 1 item
tupla = ("A",)


# len() retona o tamanho da tupla
len((0, 1, 1, 2)) # retorna 4


"""
!!! Acessar um index em uma tupla é igual a acessar em uma lista
!!! Tuplas são imutáveis
"""


# Usar o sinal + entre duas tuplas ou mais tuplas as une
tupla = (1, 2, 3, 4)
tupla2 = ("A", "B", "C")
tupla = tupla + tupla2 # tupla se torna (1, 2, 3, 4, "A", "B", "C")


# join() junta todos os elementos de uma tupla em uma string (porém todos os elementos da tupla devem ser strings)
tupla = [1, 2, 3, 4]
"".join(tupla) # retorna um erro

tupla2 = ["A", "B", "C"]
"".join(tupla2) # retorna "ABC"

tupla3 = ["A", "B", "C"]
"--".join(tupla2) # retorna "A--B--C"

tupla4 = ["1", "2", "3"]
"Pewpew".join(tupla2) # retorna "1Pewpew2Pewpew3"


# Verificar se um objeto existe em uma tupla
"C" in ("A", "B", "C") # Retorna True


# Alterando um valor em uma tupla
tupla = (1, 2, 3)
temp = list(tupla)
temp.append(4)
tupla = tupla(temp)
