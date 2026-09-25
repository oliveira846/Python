distancia = float(input("Qual a distancia da velocidade em KM: "))

if(distancia <= 200):
    print("O valor da passagem é de R${:.2f}".format(distancia * 0.50))
else:
    print("O valor da passagem é de R${:.2f}".format(distancia * 0.45))