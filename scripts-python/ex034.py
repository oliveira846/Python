salario = float(input("Qual o seu salário: "))


if (salario > 1250):
    print("Seu salário teve um aumento de R${:.2f}, totalizando {:.2f}".format(salario * 0.10, salario + (salario * 0.10)))
else:
    print("Seu slário teve um aumento de R${:.2f}, totalizando {:.2f}".format(salario * 0.15, salario + salario + (salario * 0.15)))