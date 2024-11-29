import random

def imprimir_tabuleiro(jogador_posicao, objetivo_posicao):
    for i in range(1, 11):
        if i == jogador_posicao:
            print("J", end=" ")
        elif i == objetivo_posicao:
            print("O", end=" ")
        else:
            print("-", end=" ")
    print("\n")

def mover_jogador(posicao_atual, movimento):
    nova_posicao = posicao_atual + movimento
    if nova_posicao < 1:

        nova_posicao = 1
    elif nova_posicao > 10:
        nova_posicao = 10
    return nova_posicao

def jogo_da_gloria():
    jogador_posicao = 1
    objetivo_posicao = random.randint(1, 10)

    while True:
        imprimir_tabuleiro(jogador_posicao, objetivo_posicao)

        # Verificar se o jogador atingiu o objetivo
        if jogador_posicao == objetivo_posicao:
            print("Parabéns! Você chegou ao objetivo!")
            break

        # Obter a entrada do jogador
        movimento = input("Digite 'a' para mover para a esquerda, 'd' para mover para a direita: ")

        # Mover o jogador com base na entrada
        if movimento == 'a':
            jogador_posicao = mover_jogador(jogador_posicao, -1)
        elif movimento == 'd':
            jogador_posicao = mover_jogador(jogador_posicao, 1)
        else:
            print("Entrada inválida. Use 'a' ou 'd'.")

if __name__ == "__main__":
    jogo_da_gloria()
