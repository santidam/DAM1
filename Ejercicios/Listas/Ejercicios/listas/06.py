import random
lista = []
for i in range(10):
    numeros = random.randint(-100000, 100000)
    lista.append(numeros)
    lista.sort()
print(lista)
    