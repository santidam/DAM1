casos = int(input())
for _ in range(casos):
    lista = input().split(" ")
    for k in range(len(lista)):
        lista[k] = int(lista[k])
    lista2 = []
    del lista[0]
    if len(lista) >= 1:
        for i in range(10):
            lista2.append(lista.count(i))
        for j in lista2:
            print(j, end=" ")
        print()