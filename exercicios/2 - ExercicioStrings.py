
palavra = input("Digite a palavra: ")

# Questão 1 #
qnt = input("Digite a quantidade de repetições: ")

if qnt.isdigit():
    print("Palavra multiplicada: " + palavra * int(qnt))
else:
    raise Exception("Digite quantidade válida")

# Questão 2 #
print("Palavra Invertida: " + palavra[::-1])

# Questão 3 #
frase = "Já pensou como o avião voa alto?"
print(frase.replace("avião", "barco"))

# Questão 4 #
frase = "Uma cesta não é a mesma coisa que cesta feira! Mas espera, não é cesta, é sexta"
print("Quantidade da palavra 'cesta': ", frase.lower().count("cesta"))

# Questão 5 #
boolean = False
print("Conversão de boolean para String: " + str(boolean))

# Questão 6 #
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
print("Meu nome é " + nome + " e tenho " + idade + " anos " + " e já tenho " + altura + " de altura. ")

# Questão 7 #
km = int(input("Digite uma kilometragem: "))
print(km * 27.778)

# Questão 8 #
numeroGrande = input("Digite seu cartão de crédito: ")
print("*" * (len(numeroGrande) - 4) + numeroGrande[-4:])






