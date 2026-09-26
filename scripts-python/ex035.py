print("Descubra se 3 lados formam um triangulo!")

numeroA = int(input("Digite o primeiro lado: "))
numeroB = int(input("Digite o segundo lado: "))
numeroC = int(input("Digite o terceiro lado: "))
listaLados = [numeroA, numeroB, numeroC]
listaLados.sort()

if ((listaLados[0] + listaLados[1]) > listaLados[-1]):
    print("É possivel formar um triangulo!")
else:
    print("Não é possivel formar um triangulo")