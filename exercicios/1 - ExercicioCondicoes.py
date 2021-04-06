num = int(input("Digite um Número: "))

# 1) Topico - Verificação da tipagem da variável #
if isinstance(num, int):
    print(num)
else:
    raise Exception("Erro ! Foi digitado uma String")

# 2) Topico - Verificação if's #
if num < 50:
    print("Está okay")
elif num < 75:
    print("Ta complicando")
else:
    print("Tá dificil")

# 3) Topico - Cálculo de módulo #
num1 = int(input("Digite o primeiro Número: "))
num2 = int(input("Digite o segundo Número: "))
num3 = int(input("Digite o terceiro Número: "))

if num1 % num2 == 0 and num1 % num3:
    print(True)
else:
    print(False)


