filas, columnas = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(filas)]
factor = int(input())
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] *= factor
for fila in matriz:
    print(*fila)
