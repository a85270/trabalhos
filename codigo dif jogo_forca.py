import string
import random

def jogar_forca():
    print("*************************")
    print("**Jogo da Forca!******")
    print("*************************")

    palavra_secreta = receber_palavra_secreta()
    palavra_adivinhada = "_" * len(palavra_secreta)
    letras_tentadas = []

    print("A palavra tem " + str(len(palavra_secreta)) + " letras")
    print("As letras erradas tentadas são: ", letras_tentadas)
    print("A palavra secreta é: ", palavra_adivinhada)

    tentativas = 0
    erradas = 0
    while True:
        tentativas += 1
        print("Digite uma letra ou sair")
        letra = input(">").lower()
        if letra == "sair":
            print("Fim do jogo!")
            break

        if letra in letras_tentadas:
            print("Você já tentou a letra ", letra)
            continue

        if letra in palavra_secreta:
            index = 0
            for char in palavra_secreta:
                if char == letra:
                    palavra_adivinhada = palavra_adivinhada[:index] + letra + palavra_adivinhada[index+1:]
                index += 1
        else:
            print("Você errou a letra!")
            letras_tentadas.append(letra)
            erradas += 1
            print(" " * 100, end="\r")
            desenhar_boneco(erradas)

        print("A palavra secreta é: ", palavra_adivinhada)
        if tentativas >= 7:
            print("Você perdeu! A palavra era " + palavra_secreta)
            break
        if "_" not in palavra_adivinhada:
            print("Parabéns, você ganhou!")
            break

def desenhar_boneco(erros):
    print(" ______")
    print(" |      |")
    if erros >= 1:
        print(" |      O")
    else:
        print(" |       ")
    if erros >= 2:
        print(" |    \\ /")
    else:
        print(" |       ")
    if erros >= 3:
        print(" |     \\|/")
    else:
        print(" |       ")
    if erros >= 4:
        print(" |      /")
    else:
        print(" |       ")
    if erros >= 5:
        print(" |    / ")
    else:
        print(" |       ")
    if erros >= 6:
        print("_|_/   \\_")
    else:
        print(" |       ")

def receber_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def main():
    jogar_forca()

if __name__ == "__main__":
    main()