class Partida():

    def __init__(self, jogador_um, jogador_dois): # Construtor da classe
        self.jogador_um = jogador_um
        self.jogador_dois = jogador_dois

    def jogar(self): # Método para iniciar o jogo
        count_jogador1 = 0
        count_jogador2 = 0
        count_Empate = 0

        for round in range(3):
            if self.jogador_um.cartas[round] == self.jogador_dois.cartas[round]:
                print("Round("+str(round+1)+") - Empate")
                count_Empate += 1
                if count_Empate == 3:
                    return print("Todos os rounds Empataram !")
            else:
                if self.jogador_um.cartas[round] == 1:
                    if self.jogador_dois.cartas[round] == 2:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

                if self.jogador_um.cartas[round] == 2:
                    if self.jogador_dois.cartas[round] == 3:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

                if self.jogador_um.cartas[round] == 3:
                    if self.jogador_dois.cartas[round] == 1:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

        if count_jogador1 == count_jogador2:
            return print("Empate ")

        if count_jogador1 > count_jogador2:
            return print("Jogador 1 - Venceu")
        return print("Jogador 2 - Venceu")