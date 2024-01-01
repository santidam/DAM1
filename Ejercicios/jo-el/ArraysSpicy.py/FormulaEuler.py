casos = int(input())
for _ in range(casos):
    cantidad = int(input())
    numeros = input().split(" ")
    lista = []
    lista2 = []
    for i in range(cantidad):
        lista.append(int(numeros[i]))
    lista.sort()
    for j in range(cantidad):
        if j == 0:
            lista2.append(lista[j]+lista[-1])
        elif j < cantidad/2:
            lista2.append(lista[j]+lista[-j-1])
    for k in range(len(lista2)):
        print(lista2[k], end=" ")
    print()
