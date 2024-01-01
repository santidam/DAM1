numeros = input()
datos = numeros.split(" ")
filas = int(datos[0])
columnas = int(datos[1])
precios = []
for i in range(filas):
    precio = list(map(int, input().split()))
    precios.append(precio)
    mult = int(input())
    preciosNuevos = []
    for precio in precios:
        nueva_fila = [precios * mult for precios in precio]
        preciosNuevos.append(nueva_fila)
        for precio in preciosNuevos:
            print(*precio)
