casos = int(input())
for _ in range(casos):
    diccionario = {}
    lineas = int(input())
    for __ in range(lineas):
        mapa = input()
        if mapa in diccionario:
            diccionario[mapa] += 1
        diccionario[mapa] = 1
    ganador = ""
    votos = 0
    for x, y in diccionario.items():
        if y > votos:
            votos = y
            ganador = x
    print(ganador)
