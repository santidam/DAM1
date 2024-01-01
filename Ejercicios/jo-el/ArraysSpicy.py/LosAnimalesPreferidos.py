casos = int(input())
for _ in range(casos):
    lista = []
    lineas = int(input())
    for i in range(lineas):
        if i != lineas - 1:
            animal = input()
            lista.append(animal)
        else:
            buscar = input()
    if buscar in lista:
        print("SI")
    else:
        print("NO")
