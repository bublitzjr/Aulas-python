symbol = "!@#$%^&*()_-+={}[]"

def numberOfCharacters(password):
    bonus = len(password)*4
    return bonus

def lettersOnly(password):
    return len(password)*-1

def upperCaseLetters(password):
    charsUpper = 0
    for i in password:
        if i.isupper():
            charsUpper = charsUpper + 1
    return (len(password)-charsUpper)*2

def lowerCaseLetters(password):
    charsLower = 0
    for i in password:
        if i.islower():
            charsLower = charsLower + 1
    return (len(password)-charsLower)*2

def numbers(password):
    charsNumber = 0
    for i in password:
        if i.isdigit():
            charsNumber = charsNumber + 1
    return (charsNumber*4)

def symbols(password):
    charsSymbol = 0
    for i in password:
        if i in symbol:
            charsSymbol = charsSymbol + 1
    return (charsSymbol*6)

def middleNumberOrSymbol(password):
    CharsMiddle = 0
    for i in range(1, len(password), 1):
        if (password[i].isdigit() or password[i] in symbol) and not password[i].index() == len(password):
            CharsMiddle = CharsMiddle + 1
    return (CharsMiddle*2)

def consecutiveLowerCase(password):
    qnt = 0
    for i in range(1, len(password), 2):
        if password[i].islower() and password[i+1].islower():
            qnt = qnt + 2
        return (qnt*2)*-1

password = input("Digite sua senha: \n")
bonus  = numberOfCharacters(password)
print(numberOfCharacters(password), "% Numeros")
bonus += upperCaseLetters(password)
print(upperCaseLetters(password), "% Upper case")
bonus += lowerCaseLetters(password)
print(lowerCaseLetters(password), "% lower case")
bonus += numbers(password)
print(numbers(password), "% numeros")
bonus += symbols(password)
print(symbols(password), "% simbolos")
bonus += middleNumberOrSymbol(password)
print(middleNumberOrSymbol(password), "% middle")


#bonus += consecutiveLowerCase(password)
#bonus += lettersOnly(password)




