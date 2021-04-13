# 1 = Pedra
# 2 = Papel
# 3 = Tesoura

from random import randint

class Jogadores:
    nome: str
    cartas = []

    def __init__(self, nome): # Construtor da classe
            self.nome = nome
            self.cartas = []

    def distribuir_cartas(self) -> list: # Retorno uma lista com as cartas
        for i in range(3):
             carta = randint(1, 3)
             self.cartas.append(carta)
        return self.cartas

    def traduzir_cartas(self) -> list: # Traduz a cartas pro front
        cartasTraduzidas = []
        for i in self.cartas:
            if i == 1:
                cartasTraduzidas.append("Pedra")
            elif i == 2:
                cartasTraduzidas.append("Papel")
            else:
               cartasTraduzidas.append("Tesoura")

        return cartasTraduzidas

    def limpar_cartas(self): # Limpa lista
        return self.cartas.clear()