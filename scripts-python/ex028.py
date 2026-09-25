import random

numeroAleatorio = random.randint(0, 5)
numeroChute = int(input("Qual é o seu chute? "))

if (numeroChute == numeroAleatorio):
    print("Você acertou")
else:
    print("Você errou")