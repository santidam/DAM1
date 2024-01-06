import random
entero = int(input("Introduce un número entero : "))
numero = random.randint(-10,10)
positivos = 0
negativos = 0
if entero <= 0:
    while entero <= 0:
        entero = int(input("Error, introduce un número mayor a 0: "))
else:
    for x in range(entero):
        numero = random.randint(-10, 10)
        print(numero)
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    print("negativos = ",negativos, "positivos = ",positivos)



