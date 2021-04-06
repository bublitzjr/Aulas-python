listaNumeros = [1, 2, 3]

# Questão 1 #
valor = input("Digite um valor que deseja inserir: ")
listaNumeros.append(int(valor))

# Questão 2 #
print("Favor escolha uma posição para retirar um dado:")
print(listaNumeros)
valorRetirado = input("Digite a posição a ser retirada: ")
listaNumeros.pop(int(valorRetirado))
print(listaNumeros)

# Questão 3 #
listaAnimal = ["Rabo", "Torso", "Cabeça"]
listaAnimal.reverse()
print(listaAnimal)

