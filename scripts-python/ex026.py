frase = input("Digite uma frase: ").lower().strip()

print("A letra 'a' aparece {} vezes".format(frase.count("a")))
print("A letra 'a' aparece na posição {} pela primeira vez".format(frase.find("a") + 1))
print("A letra 'a' aparece na posição {} pela ultima vez ".format(frase.rfind("a") + 1))