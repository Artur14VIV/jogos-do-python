import sys


ganhou = "Você acertou! Descubra o próximo!"
acertos = 0
numero = 12
total_tentativas = 3


print("--- JOGO DE ADIVINHAÇÃO ---")


while total_tentativas > 0:
   chute = int(input(f"\nTentativas restantes: {total_tentativas}. Digite um número de 1 à 50: "))


   if chute == numero:
       acertos += 1
       total_tentativas -= 1
       if acertos == 3:
           print("VOCÊ GANHOU!!!!!!!!!!!!!")
           sys.exit()
       else:
           print(ganhou)
           numero += 10
   else:
       total_tentativas -= 1
       if total_tentativas > 0:
           print("Você errou, continue tentando.")


   # O erro estava aqui: faltava a vírgula antes de 'numero'
   if total_tentativas == 0 and acertos < 3:
       print("GAME OVER! Você não acertou tudo.")
       print("O número era:", numero)  # Adicionada a vírgula aqui
       print("Jogue de novo recarregando a página.")
       sys.exit()
   if chute> numero:
     print("o número é menor")
   elif chute < numero:
     print("o número é maior")
