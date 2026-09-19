n1 = int(input('digite um número: '))

print('O antecessor do número {0} é {1} e o sucessor do número {0} é {2}'.format(n1, n1 - 1, n1 + 1))

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('O dobro do número {0} é {1}, o triplo do {0} é {2} e a raiz quadrada do número {0} é {3:.2f}'.format(n1, n1*2, n1*3, n1**(1/2)))

#Desevolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('a média das nota {} e {} é: {}'.format(nota1, nota2, (nota1 + nota2) / 2))

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Quantos metros: '))
print ('A conversão de {} metros para centimetros é {} e em milimetros é {}'.format(metros, metros * 100, metros * 1000))

#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

tabuada = int(input('Digite um núemro para calcular a tabuada do mesmo: '))
print('A tabuada de {0} é: \n{0}x0={1}\n{0}x1={2}\n{0}x2={3}\n{0}x3={4}\n{0}x4={5}\n{0}x5={6}\n{0}x6={7}\n{0}x7={8}\n{0}x8={9}\n{0}x9={10}\n{0}x10={11}'.format(tabuada,tabuada*0,tabuada*1,tabuada*2,tabuada*3,tabuada*4,tabuada*5,tabuada*6,tabuada*7,tabuada*8,tabuada*9,tabuada*10))

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dinheiro = float(input('Quanto dinheiro tem na carteira: '))
print('Com {} reais, você pode comprar {:.2f} dólares'.format(dinheiro, dinheiro / 5.27))

#Crie um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
area = altura * largura
print('A área da parede é {} e a quantidade de tinta necessária é {} litros'.format(area, area / 2))
