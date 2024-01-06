casos= int(input())
for _ in range(casos):
    datos = input()
    lista = datos.split(" ")
    ganador = -999
    for i in range(1, int(lista[0]) + 1):
        if int(lista[i]) > int(ganador):
            ganador = lista[i]
    print(lista.index(ganador,1))

