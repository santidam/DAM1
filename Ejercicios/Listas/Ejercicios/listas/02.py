import random
lista = []
numeros = 1
x = random.randint(1, 10)

while numeros <=10:
    lista.append(x)
    numeros += 1
    x = random.randint(1, 10)

print(f"{lista}")
for i in lista:
    print(f"Cuadrado de {i}: {i*i}\n"
          f"Cubo de {i}: {i*i*i}")

