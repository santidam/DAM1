casos = int(input())
for _ in range(casos):
    lista = input().split(" ")
    inicio = int(lista[0])
    desplazamiento = 0
    for i in range(1, 4):
        if inicio != 8:
            if int(lista[i]) + inicio == 8:
                inicio = 8
            elif int(lista[i]) + inicio > 8 and int(lista[i]) + inicio != 8:
                desplazamiento = int(lista[i]) + inicio - 8
                inicio = 8 - desplazamiento
            elif int(lista[i]) + inicio < 8:
                inicio += int(lista[i])
    print(inicio)
