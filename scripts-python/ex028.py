import random
import time

numeroAleatorio = random.randint(0, 5)
print("-=-"*30)
print("Jogo da adivinhação")
print("-=-"*30)
numeroChute = int(input("Qual é o seu chute? "))

print("Processando...")
time.sleep(4)

if (numeroChute == numeroAleatorio):
    print("Você acertou")
else:
    print("Você errou")
