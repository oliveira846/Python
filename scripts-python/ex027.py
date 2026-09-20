nome = input('Digite o seu nome completo: ').title()
lista_nome = nome.split()

print('Seu nome é: {}'. format(nome))
print('Seu primeiro nome é: {} '.format(lista_nome[0]))
print('Seu último nome é: {}'.format(lista_nome[-1]))