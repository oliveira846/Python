import math


angulo = float(input("Digite o angulo: "))
rad = math.radians(angulo)


print("O coseno é: {:.2f}\nO seno é {:.2f}\nE a tangente é {:.2f}".format(math.cos(rad), math.sin(rad), math.tan(rad)))