casos = int(input())
for _ in range(casos):
    diccionario = {}
    diccionario["paises"] = {}
    lineas = int(input())
    for __ in range(lineas):
        if __ <= lineas - 2:
            paisCapital = input().split("-")
            pais = paisCapital[0]
            capital = paisCapital[1]
            diccionario["paises"].update({pais: capital})
        else:
            nombre = input()
    print("{", end="")
    for x, y in diccionario.items():
        for j, k in y.items():
            if j != pais:
                print(f"{j}={k}, ", end="")
            if j == pais:
                print(f"{j}={k}", end="")
    print("}")
    for x, y in diccionario.items():
        for j, k in y.items():
            if k == nombre:
                print(j)
