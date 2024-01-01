casos = int(input())
for _ in range(casos):
    cantidad = int(input())
    lista = input().split()
    posicion = int(input())
    del lista[posicion]
    for i in lista:
        print(i, end=" ")
    print()
