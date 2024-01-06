casos = int(input())
for _ in range(casos):
    corredores = int(input())
    diamante = 0
    for i in range(corredores):
        camino = input()
        for j in range(len(camino)):
            if j < len(camino) -1:

                if camino[j] == "{" and camino[j+1] == "}":
                    diamante += 1
    print(diamante)