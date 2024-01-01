k = int(input())
for i in range(k):
    n = input()
    datos = n.split(" ")
    vida = int(datos[0])
    daño = int(datos[1])
    if daño < vida:
        if daño > vida * 0.2:
            print("Momento Banana")
        else:
            print("Nope")
    else:
        print("Nope")
