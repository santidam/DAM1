k = int(input())
for i in range(k):
    mediciones = input()
    numeros = mediciones.split(" ")
    n1 = int(numeros[0])
    n2 = int(numeros[1])
    n3 = int(numeros[2])
    n4 = int(numeros[3])
    n5 = int(numeros[4])
    if n1 >= 10000 or n2 >= 10000 or n3 >= 10000 or n4 >= 10000 or n5 >= 10000:
        print("M")
    elif 1000 <= n1 < 10000 or 1000 <= n2 < 10000 or 1000 <= n3 < 10000 or 1000 <= n4 < 10000 or 1000 <= n5 < 10000:
        print("B")
    else:
        print("H")
