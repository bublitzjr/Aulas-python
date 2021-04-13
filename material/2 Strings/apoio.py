# T e s t e
# 0 1 2 3 4 - Posições

#  T  e  s  t  e
# -5 -4 -3 -2 -1 - Posições

string = "Banana"

string
# e 
"Banana"
# são exatamente a mesma coisa


# Acessando um index só
"Teste"[1] # retorna "e"
"Teste"[-2] # retorn "t"


# Acessando por vários indexes
"Teste"[0:3] # retorna "Tes"
"Teste"[0:] # retorna "Teste"
"Teste"[:4] # retorna "Test" 
"Teste"[:] # retorna "Teste"
"Teste"[-5:-2] # retorna "Tes"

# Usando o passo
"Teste"[::2] # retorna "Tse"
"Teste"[1:4:2] # retorna "et"
"Teste"[::-1] # retorna "etseT"


# index() retorna o index de uma string dentro de outra
"Eu tenho uma banana".index("bana") # retorna 13
"Bananas são amarelas".index("Bananas") # retorna 0
# "Bananas são amarelas".index("bananas") # retorna um erro porque a string não está dentro da outra


# in retorna se uma string está dentro de outra
"ana" in "Banana" # retorna True
"la" in "Banana" # retorna False


# Juntando strings
"Banana" + "e uma" + "maçã" # retorna "Banana e uma maçã"


# Multiplicando strings
"Banana" * 5 # retorna "BananaBananaBananaBananaBanana"
"Banana" + "Oi" * 2 # retorna "BananaOiOi"
("Banana" + "Oi") * 2 # retorna "BananaOiBananaOi"


# Maiusculo, minusculo e capitalizado
"banana".upper() # retorna "BANANA"
"BaNaNa".lower() # retorna "banana"
"isso é isso!".capitalize() # retorna "Isso é isso!"


# replace() retorna uma string com os caracteres replacados
"Pense em uma frase legal".replace("legal", "chata") # retorna "Pense em uma frase chata"


# split() retorna uma lista da string, separada por um caractere escolhido (padrão espaço " ")
"Isso é banana".split() # retorna ['Isso', 'é', 'banana']
"Isso é banana".split("é") # retorna ['Isso ', ' banana']
"Isso;é;banana".split(";") # retorna ['Isso', 'é', 'banana']


#  count() retorna a contagem de quantas vezes uma string aparece
"banana não é banana se não for amarela".count("banana") # retorna 2
"Uma pedra".count("pedra") # retorna 1


# Verifica se é número(isdigit), letra(isalpha) ou é os dois(isalnum)
"Banana123".isdigit() # retorna False
"Banana".isdigit() # retorna False
"123".isdigit() # retorna True

"Banana123".isalpha() # retorna False
"Banana".isalpha() # retorna True
"123".isalpha() # retorna False

"Banana123".isalnum() # retorna True
"123".isalnum() # retorna True
"$%#@".isalnum() # retorna False


# Formatando por f""
animal = "baleia"
animal2 = "golfinho"
f"Aqui, olha esse(a) {animal} e esse(a) {animal2}" # retrona "Aqui, olha esse(a) baleia e esse(a) golfinho"


# Formatando por .format()
"Teste {0} e {1}".format("Número 11", "Número 2") # retorna "Teste Número 11 e Número 2"
# ou
"Teste {um} e {dos}".format(um="Número 13", dos="Número 2") # retorna "Teste Número 13 e Número 2"