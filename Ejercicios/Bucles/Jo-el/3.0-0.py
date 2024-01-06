entero = int(input("Introduce un número entero positivo: "))
positivo = 0
negativo = 0
if entero <= 0:
    while entero <= 0:
        entero = int(input("Error, introduce un número mayor a 0: "))
else:
    for n in range(1, entero + 1):
        entero = int(input("Introduce  un número entero: "))
        if entero > 0:
            positivo += 1
        elif entero <0:
            negativo += 1
    print("positivos: ", positivo, "negativos: ", negativo)