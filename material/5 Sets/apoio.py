# Criando um set
"""
x = {}
ou
x = set()
"""


"""
!!!
Sets são criado de forma totalmente aleatória

Sets não podem ter valores dupicados, então eles são ignorados

Sets, após criados, seus valores são imutáveis (porém, novos valores podem ser adicionados)
!!!
"""

# sets não podem ser acessados por index, porém podem ser percorridos em um 'for'
my_set = {1, "A", 1.8}
for i in my_set:
    i # Retorna 1, "A",  1.8 (porém não será sempre nessa ordem)


# Adicionando itens à um set
my_set = {1, 2, 3}
my_set.add(4)
my_set # Retorna {1, 2, 3, 4}


# Juntar sets
my_set = {1, 2, 3}
other_set = {4, 5, 6}
my_set.update(other_set)
my_set # Retorna {1, 2, 3, 4, 5, 6}

# A função update pode receber qualquer iterável
my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
my_set # Retorna {1, 2, 3, 4, 5, 6}


# Removendo itens do set
my_set = {"A", "B", "C"}
my_set.remove("A")
# Com remove(), caso não exista o objeto dentro do set, será lançada uma excessão

my_set = {"A", "B", "C"}
my_set.discard("A")
# Com discard(), caso não exista o objeto dentro do set, não será lançado nada

my_set = {"A", "B", "C"}
my_set.pop() # Removerá a última posição do set
# !!! Como sets sempre mudam de ordem, nunca se sabe o que está na última posição, então, cuidado!


# Limpa o set
my_set = {"A", "B", "C"}
my_set.clear()


# Deleta o set
my_set = {"A", "B", "C"}
del my_set
