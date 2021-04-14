from random import randint


class Jogo:

    """
    0 = pedra
    1 = papel
    2 = tesoura
    """

    correlacao_carta_numero = {0: "pedra", 1: "papel", 2: "tesoura"}

    def distribuir_cartas(self):
        cartas_criadas = [randint(0, 2) for i in range(3)]
        cartas_convertidas = self.converter_numeros_para_cartas(cartas_criadas)
        return cartas_convertidas

    def converter_numeros_para_cartas(self, cartas: list):
        return [self.correlacao_carta_numero[i] for i in cartas]

    def iniciar_rodada(self, cartas_e_jogadores: dict):
        resultado = self.verificar_quem_ganhou(cartas_e_jogadores)
        if resultado[0]:
            return True, f"{resultado[1]} ganhou a rodada!!!"
        return False, "Deu empate!"

    def verificar_quem_ganhou(self, cartas_e_jogadores: dict):

        pedra_tesoura_ganhador = self.verificar_carta_ganhadora(cartas_e_jogadores, "pedra", "tesoura")
        if pedra_tesoura_ganhador[0]:
            return pedra_tesoura_ganhador

        papel_pedra = self.verificar_carta_ganhadora(cartas_e_jogadores, "papel", "pedra")
        if papel_pedra[0]:
            return papel_pedra

        tesoura_papel = self.verificar_carta_ganhadora(cartas_e_jogadores, "tesoura", "papel")
        if tesoura_papel[0]:
            return tesoura_papel

        return (False,)

    def verificar_carta_ganhadora(self, cartas_e_jogadores, carta_ganha, carta_perde):

        if cartas_e_jogadores[0]["carta"] == carta_ganha and cartas_e_jogadores[1]["carta"] == carta_perde:
            return True, cartas_e_jogadores[0]["nome"]
        elif cartas_e_jogadores[0]["carta"] == carta_perde and cartas_e_jogadores[1]["carta"] == carta_ganha:
            return True, cartas_e_jogadores[1]["nome"]
        return (False,)


class Jogador:

    def __init__(self, nome):
        self.nome = nome

    def criar_nova_mao(self, cartas: list):
        self.mao_atual = cartas

    def limpar_mao_atual(self):
        del self.mao_atual

    def ver_mao_atual(self):
        print(f"\n{'*'*50}\n")
        for i, carta in enumerate(self.mao_atual):
            print(f"{i+1} - {carta.capitalize()}")

    def jogar_carta(self):
        while True:
            try:
                numero_da_carta = int(input(f"\n{self.nome}, escolha uma das cartas acima: "))
                print("\n")
                return self.mao_atual[numero_da_carta-1]
            except:
                pass


def executar_jogo():
    jogo = Jogo()

    jogador1 = Jogador(input("Digite o nome do jogador número 1: "))
    jogador2 = Jogador(input("Digite o nome do jogador número 2: "))

    while True:
        print(f"\n{'-'*30}Iniciando um novo jogo!!!{'-'*30}")
        cartas_jogador1 = jogo.distribuir_cartas()
        cartas_jogador2 = jogo.distribuir_cartas()

        for i in range(3):
            jogador1.criar_nova_mao(cartas_jogador1)
            jogador2.criar_nova_mao(cartas_jogador2)

            jogador1.ver_mao_atual()
            carta_escolhida1 = jogador1.jogar_carta()
            jogador1.mao_atual.remove(carta_escolhida1)

            jogador2.ver_mao_atual()
            carta_escolhida2 = jogador2.jogar_carta()
            jogador2.mao_atual.remove(carta_escolhida2)

            cartas_e_jogadores = [dict(nome=jogador1.nome, carta=carta_escolhida1),
                                  dict(nome=jogador2.nome, carta=carta_escolhida2)]
            resultado = jogo.iniciar_rodada(cartas_e_jogadores)
            print(resultado[1])
            if resultado[0]:
                break

        jogador1.limpar_mao_atual()
        jogador2.limpar_mao_atual()


executar_jogo()

# x, y = (1, 2)
#
# lista = ["A", "B", "C"]
# for numero, valor in enumerate(lista):
#     print(f"{numero} - {valor}")
