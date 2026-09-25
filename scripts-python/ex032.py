ano = int(input("Digite o ano para saber se ele é bisexto: "))

if (ano%100 == 0 and ano%400 != 0):
    print("O ano não é bissexto!")
else:
    if (ano%4 == 0):
        print("O ano é bissexto!")
    else:
        print("O ano não é bissexto!")