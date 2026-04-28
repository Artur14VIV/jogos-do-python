import sys
import random  
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

  
    palavras = ["python", "javascript", "ruby", "java", "php"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("Regras:")
    print("1- Você tem 6 tentativas;")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    print("")
    print("Dica: é uma famosa linguagem de programação")
    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        # Desenho da forca (Mantive sua lógica, apenas corrigi a exibição)
        if erros == 1:
            print(" O ")
        elif erros == 2:
            print(" O ")
            print(" | ")
        elif erros == 3:
            print(" O ")
            print("/| ")
        elif erros == 4:
            print(" O ")
            print("/|\\")
        elif erros == 5:
            print(" O ")
            print("/|\\")
            print("/  ")
        elif erros == 6:
            print(" O ")
            print("/|\\")
            print("/ \\")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)

    if acertou:
        print("Fim do jogo, você acertou!")
    else:
        print(f"Fim de jogo, você morreu! A palavra era {palavra_secreta}")

if __name__ == "__main__":
    jogar()
