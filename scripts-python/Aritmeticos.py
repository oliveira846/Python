#numero = int(input("Qual o número: "));
#nota1 = int(input("Digite a primeira nota:"))
#nota2 = int(input("Digite a segunda nota:"))
#metros = int(input("Digite a quantidade de metros: "))
#reais = float(input("Digite a quantidade de dinheiro: "))
#largura = int(input("Digite a largura: "))
#altura = int(input("Digite a altura: "))
#area = altura * largura
#produto = float(input("Qual o valor do produto: "))
#desconto = float(input("Quanto é o desconto: "))
#totaldesc = produto - (produto*desconto/100)
#salario = float(input("Qual o seu salario: R$"))
#reajuste = float(input("De quanto foi o reajuste salarial: "))
#totalreajuste = salario + (salario*reajuste/100)
#celsius = float(input("Informe a temperatura em celsius: "))
#f = ((9*celsius)/5)+32
kmAlugado = int(input("Por quantos km o carro ficou alugado: "))
diasAlugado = int(input("Quantos dias o carro ficou alugado: "))
totalAlugado = float((diasAlugado * 60) + (kmAlugado * 0.15))

print("O carro ficou alugado por {} dias e rodou {} KM, totalizando R$ {:.2f}".format(diasAlugado, kmAlugado, totalAlugado))

#-------------------

#print("O valor do salário informado é de: R${:.2f}".format(salario))
#print("A porcentagem de reajuste é de: {}%".format(reajuste))
#print("E o seu salario com reajuste é de R${:.2f}".format(totalreajuste))

#-------------------



#-------------------

#print("A temperatura de {}C celsius, equivale a {}F em farenheit".format(celsius, f))

#-------------------

#print("O valor do produto é: R${:.2f}".format(produto));
#print("O total de desconto é: {}%".format(int(desconto)));
#print("O desconto foi de R${:.2f} e o total com desconto é R${:.2f}".format(totaldesc,produto*desconto/100));

#-------------------

# print("A sucessor de {0} é {1} e o antecessor de {0} é {2}".format(numero, numero + 1, numero - 1))

#-------------------

#print("o dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(numero, numero * 2, numero * 3, numero**(1/2)))

#-------------------

#print("A primeira nota é {}, a segunda nota é {} e a média delas é {}".format(nota1, nota2, (nota1 + nota2)/2))

#-------------------

#print("A metragem é de {} \nconvertido em centimetros é {}\nconvertido em milimetros é {}\nconvertido em KM é {}\nconvertido em convertido em hectômetro é {}\ne convertido em decâmetro é {}".format(metros, metros * 100, metros * 1000, metros / 1000, metros / 100, metros / 10))

#-------------------

#print("a tabuada de {0} é:\n{0} x 1 = {1}\n{0} x 2 = {2}\n{0} x 3 = {3}\n{0} x 4 = {4}\n{0} x 5 = {5}\n{0} x 6 = {6}\n{0} x 7 = {7}\n{0} x 8 = {8}\n{0} x 9 = {9}\n{0} x 10 = {10}".format(numero,numero * 1,numero * 2,numero * 3,numero * 4,numero * 5,numero * 6,numero * 7,numero * 8,numero * 9,numero * 10))

#-------------------

#print("Você tem R${:.2f} e convertido para dolares fica ${:.2f}".format(reais, reais/3.27))

#-------------------

#print("A area de {} de altura e {} de largura é {} e a quantidade de tinta necessaria é {}".format(altura, largura, area, area / 2))