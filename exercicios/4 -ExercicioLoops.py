primeiraFase = [5, 9, 3, 5, 2, 1, 6, 3]
segundaFase = []
final = []

def CalcularFase(Fase, proximaFase):
    if (len(Fase) != 2):
        for i in range(0, len(Fase), 2):
            if Fase[i] != Fase[i + 1]:
                maior = max(Fase[i], Fase[i + 1])
                proximaFase.append(maior)
            else:
                proximaFase.append(0)
        return proximaFase
    else:
        return max(Fase[0], Fase[1])

print("Primeira Fase: ", primeiraFase)

print("Segunda Fase:  ", CalcularFase(primeiraFase, segundaFase))

print("Final:         ", CalcularFase(segundaFase, final))

print("Vencedor:      ", CalcularFase(final, 0))

print("================== \n")

# Questão 2 #
palavras = ["Banana", "Maçã", "Pepino", "Batata"]
print("!!!".join(palavras).upper().replace("A", "@"))

