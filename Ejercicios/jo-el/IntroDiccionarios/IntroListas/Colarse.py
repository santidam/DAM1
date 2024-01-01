casos = int(input())
for _ in range(casos):
    numeroElementos = int(input())
    lista = input().split(" ")
    colados = input().split(" ")
    colado = colados[0]
    posicionColado = int(colados[1])
    lista.insert(posicionColado, colado)
    for i in lista:
        print(i, end=" ")
    print()
