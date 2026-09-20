numero = input("Digite um numero de até 4 digitos: Ex. 9999  ")
numero_lista = " ".join(numero)
numero_lista = numero_lista.split()


numero_lista.reverse()
numero_lista.extend(["Não tem número "]*4)

#print(numero_lista)

print("A unidade é: {}\nA dezena é: {}\nA centena é: {}\nO milhar é: {}".format(numero_lista[0], numero_lista[1], numero_lista[2], numero_lista[3]))