def somar(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    return num1 / num2

def multiplicacao(num1, num2):
    return num1 * num2

primeiroValor = int(input("Digite primeiro valor: "))
segundoValor  = int(input("Digite segundo valor: "))
operacao      = input("Funções: + .. - .. * .. /\n"
                      "Escolha uma operação: ")

if operacao == "+":
    print(somar(primeiroValor, segundoValor))
elif operacao == "-":
    print(subtracao(primeiroValor, segundoValor))
elif operacao == "*":
    print(multiplicacao(primeiroValor, segundoValor))
else:
    print(divisao(primeiroValor, segundoValor))

