velocidade = float(input("Digite a velocidade em km: "))

if (velocidade > 80):
    print("Você foi multado! o valor da multa foi de R${:.2f}".format(float(velocidade - 80) * 7))
else:
    print("Você não foi multado")