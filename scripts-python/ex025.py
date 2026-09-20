nome = input("Digite o seu nome completo: ").lower()
lista_nome = nome.split()

if lista_nome.count("silva") >= 1:
    print("Parabeeeeens, seu nome tem Silva")
else: 
    print("Infelizmente você não faz parte da família Silva")