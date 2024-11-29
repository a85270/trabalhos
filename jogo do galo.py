def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(simbolo == jogador for simbolo in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha a linha (1-3) e coluna (1-3): ").split())
        linha -= 1
        coluna -= 1

        if linha < 0 or linha >= 3 or coluna < 0 or coluna >= 3 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break

        if jogadas == 9:
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()
