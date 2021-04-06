# Declaração de variável
x = 1
y = "Teste"
_nome = "Gustavo"
Altura = 1.8


# Eclusão de uma variável
del x
del y
del _nome
del Altura


# Declarando várias variaveis com o mesmo valor
x = y = z = "Um valor aí"


# Declarando várias variaveis com o vários valores
x, y, z = "Valor1", 2, True
# ou
x, y, z = ("Valor1", 2, True)


# Indentação
# x = 1
#     x = 2
# Isso retornará um erro

# x = 1
# x = 2
# Isso dará certo


# type() retorna o tipo do objeto
type(1) # retorna int
type("Teste") # retorn str


# print() mostra no console a representação de um objeto
print("OIIIIIII") # retorna "OIIIIIIII"
print("Isso", "é", "um", "teste") # retorna "Isso é um teste"
print(2 > 1) # retorna True


# input() pede algo ao usuário e espera que ele digite algo
input() # retorna só o que for digitado
input("Digite algo: ") # retorna só o que for digitado
# input() sempre retornará uma string

# len() retorna o tamanho do iterável
len("Teste") # retorna 5
len(4) # retorna erro