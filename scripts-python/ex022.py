nome = input("Digite o seu nome: ")
nome_sem_espaco = nome.replace(" ","")
lista_nome = nome.split()

print("Bem vindo, {}".format(nome))
print("Seu nome em letra maiuscula é: {}".format(nome.upper()))
print("Seu nome em letra mniuscula é: {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome_sem_espaco)))
print("E o seu primeiro nome tem {} letras".format(len(lista_nome[0])))
