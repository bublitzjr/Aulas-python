# Cirando um tratamento de exceções
"""
try:
    comandos...
except:
    comandos...
"""
try:
    print(10 / 0)
except:
    print("Não é possível dividir por zero!")

try:
    pass
except:
    pass

# Except é ativado quando algum erro ocorre dentro d o bloco 'try'
# Caso nenhum erro ocorra, except é ignorado


# Usando except e definindo qual erro ele deve tratar
try:
    pass
except IndexError: # Aqui, ele tratará somente quando o erro ocorrido for do tipo IndexError
    pass
except ZeroDivisionError: # Aqui, ele tratará somente quando o erro ocorrido for do tipo ZeroDivisionError
    pass
except:
    pass # Aqui tratará todos os erros que não forem citados anteriormente


# Usando else
try:
    pass
except:
    pass
else:
    pass
# 'else' é ativado caso não ocorra nenhum erro durando o bloco 'try'


# Usando finally
try:
    pass
except:
    pass
finally:
    pass

# Caso queira colocar também o else, a ordem deve ser try - except - else - finally


# Lançar uma exceção genérica
# raise Exception("Mensagem")

# Lançar um erro expecífico
# raise ZeroDivisionError("Mensagem")

# Lançar uma exceção caso um condição seja falsa
# assert 1 == 1, "Mensagem" # Não lança nada
# assert 1 == 2, "Mensagem" # Lança uma exceção tipo Assert