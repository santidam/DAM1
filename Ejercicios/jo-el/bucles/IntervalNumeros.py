numero = input()
datos = numero.split(" ")
n1 = int(datos[0])
n2 = int(datos[1])
if n1 >= n2:
    for i in range(n1, n2 - 1, -1):
        print(i)
else:
    print("El segon numero no es mes petit que el primer")
