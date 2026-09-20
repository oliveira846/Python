cidade = input("Digite o nome da sua cidade: ")
lista_cidade = cidade.split()

if lista_cidade[0].lower() == "santo":
    print("Sua cidade começa com Santo")
else:
    print("Sua cidade não começa com Santo")