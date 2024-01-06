casos = int(input())
for _ in range(casos):
    entrada = int(input())
    datos = input()
    lista = datos.split(" ")
    cambio = input()
    cambios = cambio.split(" ")
    cambio1 = cambios[0]
    cambio2= cambios[1]
    for i in range(len(lista)):
        if lista[i] == cambio1:
            lista[i] = cambio2
    for j in range(len(lista)):
        print(lista[j], end=" ")
    print()