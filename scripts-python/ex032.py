from datetime import date

ano = int(input("Digite o ano para saber se ele é bisexto: Digite 0 para analiser o ano atual! "))

if ano == 0:
    ano = date.today().year
    
if (ano%100 == 0 and ano%400 != 0):
    print("O ano {} não é bissexto!".format(ano))
else:
    if (ano%4 == 0):
        print("O ano {} é bissexto!".format(ano))
    else:
        print("O ano {} não é bissexto!".format(ano))