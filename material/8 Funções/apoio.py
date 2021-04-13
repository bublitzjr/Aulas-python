# Criando uma função
"""
def nome_funcao():
    comandos...
"""
def teste():
    return "Oi"


# Chamando uam função
def teste():
    return "Oi"

teste() # Retorna "Oi"


# Definindo parâmetros para a função
def teste(nome, idade):
    return "Seu nome é " + nome + " e sua idade é " + str(idade)

teste("Gustavo", 100) # Retorna "Seu nome é Gustavo e sua idade é 100"


# Definindo parâmetros com valor padrão
def teste(nome, idade=None):
    if idade:
        frase = nome + ", você tem " + str(idade) + " anos"
    else:
        frase = "Olá " + nome
    return frase

teste("Gustavo") # Retorna "Olá Gustavo"
teste("Gustavo", 100) # Retorna "Gustavo, você tem 100 anos"

# Parâmetros com valor padrão devem ser colocados sem no final
def teste(nome, idade, cpf=None, altura=None):
    pass


# Definindo **kwargs
def teste(**kwargs):
    kwargs # Retornará {'nome': 'Gustavo', 'idade': 1}
# **kwargs devem sempre ser definidos no final

teste(nome="Gustavo", idade=1)


# É possível passar qualquer objeto como um argumento
def teste(numeros):
    numeros # Retorna [1, 2, 3]

lista = [1, 2, 3]
teste(lista)


# Definindo o tipo do parâmetro e o tipo de saída da função
def teste(nome: str, idade: int) -> tuple:
    return nome, idade # Retorna ("Gustavo", 100)

teste("Gustavo", 100)

# Caso queira colcar o tipo do parâmetro e um valor padrão, a ordem é (parâmetro: tipo = valor_padrão)