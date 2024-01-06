casos = int(input())
for _ in range(casos):
    importe = int(input())
    peticiones = input().split(" ")
    lista = []
    contador = 0
    for i in range(len(peticiones)-1):
        if peticiones[i].isnumeric():
            lista.append(int(peticiones[i]))
    lista.sort()
    for j in range(len(lista)):
        if importe >= lista[j]:
            importe -= lista[j]
            contador += 1
    print(contador)
