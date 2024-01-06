casos = int(input())
for _ in range(casos):
    cantidad = int(input())
    datos = input()
    lista = datos.split(" ")
    medida = int(input())
    zapatoDisponible = 0
    for i in range(cantidad):
        if int(lista[i]) >= medida -1 and int(lista[i]) <= medida +1:
            zapatoDisponible += 1
    if zapatoDisponible > 0:
        print("SI")
    else:
        print("NO")

