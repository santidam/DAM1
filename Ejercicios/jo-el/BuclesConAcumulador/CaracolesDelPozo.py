k = int(input())
ciclos = 0
for i in range(k):
    datos = input()
    numeros = datos.split(" ")
    profundidat = int(numeros[0])
    subida = int(numeros[1])
    bajada = int(numeros[2])
    if bajada >= subida and subida != profundidat or subida == 0:
        print("NO")
    # elif profundidat == subida:
    #     print(0)
    else:
        while profundidat > 0:
            ciclos += 1
            profundidat -= subida
            if profundidat > 0:
                profundidat += bajada
                ciclos += 1
        if profundidat <= 0:
            print(f"{(ciclos//2) + 1}")
    ciclos = 0
