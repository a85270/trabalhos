import random

def criar_tabuleiro():
    tabuleiro = []
    for _ in range(5):
        tabuleiro.append(['O'] * 5)  # 'O' representa água
    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def posicionar_navios(tabuleiro, navios):
    for _ in range(navios):
        linha = random.randint(0, len(tabuleiro) - 1)
        coluna = random.randint(0, len(tabuleiro[0]) - 1)
        while tabuleiro[linha][coluna] == 'X':
            # Garante que não há sobreposição de navios
            linha = random.randint(0, len(tabuleiro) - 1)
            coluna = random.randint(0, len(tabuleiro[0]) - 1)
        tabuleiro[linha][coluna] = 'X'  # 'X' representa um navio

def realizar_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 'X':
        print("Parabéns! Você acertou um navio!")
        tabuleiro[linha][coluna] = 'H'  # 'H' representa um acerto
        return True
    else:
        print("Você errou. Tente novamente.")
        tabuleiro[linha][coluna] = 'M'  # 'M' representa uma tentativa sem sucesso
        return False

def verificar_fim_de_jogo(tabuleiro):
    for linha in tabuleiro:
        if 'X' in linha:
            return False  # Ainda há navios no tabuleiro
    return True            # Todos os navios foram afundados

def batalha_naval():
    print("Bem-vindo ao Jogo de Batalha Naval!")
    jogador1_tabuleiro = criar_tabuleiro()
    jogador2_tabuleiro = criar_tabuleiro()

    navios = 3  # Número de navios por jogador
    print("Posicionando navios para o Jogador 1...")
    posicionar_navios(jogador1_tabuleiro, navios)
    exibir_tabuleiro(jogador1_tabuleiro)

    print("Posicionando navios para o Jogador 2...")
    posicionar_navios(jogador2_tabuleiro, navios)
    exibir_tabuleiro(jogador2_tabuleiro)

    while True:
        print("Jogador 1:")
        linha = int(input("Digite o número da linha (0-4): "))
        coluna = int(input("Digite o número da coluna (0-4): "))
        resultado_jogada = realizar_jogada(jogador2_tabuleiro, linha, coluna)
        exibir_tabuleiro(jogador2_tabuleiro)
        if resultado_jogada and verificar_fim_de_jogo(jogador2_tabuleiro):
            print("Jogador 1 venceu!")
            break

        print("Jogador 2:")
        linha = int(input("Digite o número da linha (0-4): "))
        coluna = int(input("Digite o número da coluna (0-4): "))
        resultado_jogada = realizar_jogada(jogador1_tabuleiro, linha, coluna)
        exibir_tabuleiro(jogador1_tabuleiro)
        if resultado_jogada and verificar_fim_de_jogo(jogador1_tabuleiro):
            print("Jogador 2 venceu!")
            break

if __name__ == "__main__":
    batalha_naval()
