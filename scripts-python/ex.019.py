import random

aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")

print("Entre {}, {}, {} e {} o escolhido foi {}".format(aluno1, aluno2, aluno3, aluno4,random.choice([aluno1, aluno2, aluno3, aluno4])))
