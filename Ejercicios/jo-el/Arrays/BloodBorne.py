casos = int(input())
for _ in range(casos):
    cantidadDatos = int(input())
    datos = input()
    lista = datos.split(" ")
    si = 0
    for i in range(cantidadDatos -1):
        if lista[i] == lista[i+1]:
            si += 1
    if si > 0:
        print("SI")
    else:
        print("NO")

