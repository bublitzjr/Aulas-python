from Partida import Partida
from Jogadores import Jogadores

jogador1 = Jogadores("João")
jogador1.distribuir_cartas()
print(jogador1.nome, " - Cartas: ", jogador1.traduzir_cartas())

jogador2 = Jogadores("Maria")
jogador2.distribuir_cartas()
print(jogador2.nome, " - Cartas: ", jogador2.traduzir_cartas())

partida = Partida(jogador1, jogador2)
partida.jogar()
