import sys
def jogar():


   print("*********************************")
   print("***Bem vindo ao jogo da Forca!***")
   print("*********************************")




   palavra_secreta = "banana".upper()
   letras_acertadas = ["_", "_", "_", "_", "_", "_"]


   enforcou = False
   acertou = False
   erros = 0


   print(letras_acertadas)


   while (not acertou and not enforcou):


       chute = input("Qual letra? ")
       chute = chute.strip().upper()


       if (chute in palavra_secreta):
           index = 0
           for letra in palavra_secreta:
               if (chute == letra):
                   letras_acertadas[index] = letra
               index += 1
       else:
           erros += 1

       if erros == 1:
           print("O")
       elif erros == 2:
           print("0")
           print("|")
       if erros == 3:  # <-- Aqui começa um novo 'if'
           print(" 0")
           print("/|")
       elif erros == 4:
           print(" 0")
           print("/|\")
       if erros == 5:
           print(" 0")
           print("/||")
           print(" /  ")
       elif erros == 6:
           print("  0")
           print(" /||")
           print(" /|")

       enforcou = erros == 6
       print(letras_acertadas)
       acertou = not "_" in letras_acertadas

       if enforcou == True:
          print("Fim de jogo, você morreu")
          return
       elif not "_" in letras_acertadas:
         print("Fim do jogo, você acertou")
         return
jogar()
