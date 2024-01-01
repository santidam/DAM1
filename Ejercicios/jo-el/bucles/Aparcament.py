coche = int(input("C"))
while coche != 0:
    espacioCoche = coche * 1.5
    aux = espacioCoche * 10000
    numeros = input("n")
    aparcar = 0
    agujero = 0
    espacio = 0
    while numeros != "0":
        calle = numeros.split(" ")
        inicio = int(calle[0])
        final = int(calle[1])
        espacioCalle = final - inicio
        agujero += 1
        if espacioCalle >= espacioCoche:
            aparcar += 1
            if espacioCalle < aux:
                aux = espacioCalle
                espacio = agujero
        numeros = input("N")
    if aparcar >= 1:
        print(f"SI {espacio}")
    elif aparcar == 0:
        print("NO")
    coche = int(input("C"))
