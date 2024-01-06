lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    numero = int(input("Introduce valores para lista 1: "))
    lista1.append(numero)
for j in range(5):
    numero2 = int(input("Introduce valores para lista 2: "))
    lista2.append(numero2)
for k in range(5):
    x = lista1[k]+lista2[k]
    lista3.append(x)

print(f"Lista 1:  {lista1}\n"
      f"Lista 2: {lista2}\n"
      f"Lista 3: {lista3}")

