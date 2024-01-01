k = int(input())  # variable introducida por ususario
for i in range(1, k + 1):  # bucle for deesde el 1 hasta el nº introducido por el usuario
    # bucle dentro del bucle con iteración regresiva desde el número dado por el bucle "i" hasta el 1
    for j in range(i, 0, -1):
        # imprimimos regresion, y ajustamos en una misma línea y sin espacios
        print(j, sep="", end="")
