def criar_tabuleiro():
    return [[" " for _ in range(7)] for _ in range(6)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 21)

def fazer_jogada(tabuleiro, coluna, jogador):
    for linha in range(5, -1, -1):
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            return True
    return False

def verificar_vitoria(tabuleiro, jogador):
    for linha in range(6):
        for coluna in range(7):
            if tabuleiro[linha][coluna] == jogador:
                if (coluna <= 3 and all(tabuleiro[linha][coluna + i] == jogador
                        for i in range(4))) or (linha <= 2 and all(tabuleiro[linha + i][coluna] == jogador
                        for i in range(4))) or (coluna <= 3 and linha <= 2 and all(tabuleiro[linha + i][coluna + i] == jogador 
                        for i in range(4))) or coluna >= 3 and linha <= 2 and all(tabuleiro[linha + i][coluna - i] == jogador 
                        for i in range(4)):
                    return True
    return False

def jogo_4_em_linha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1-7): ")) - 1

        if coluna < 0 or coluna >= 7:
            print("Coluna inválida. Tente novamente.")
            continue

        if not fazer_jogada(tabuleiro, coluna, jogador_atual):
            print("Coluna cheia. Escolha outra coluna.")
            continue

        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break

        if jogadas == 42:  # Total de casas no tabuleiro
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_4_em_linha()
