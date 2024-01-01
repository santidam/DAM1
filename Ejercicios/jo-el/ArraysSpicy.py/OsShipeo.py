casos = int(input())
for _ in range(casos):
    altura = input().split(" ")
    mayor = -1000
    menor = 1000
    for i in range(1, int(altura[0])+1):
        if int(altura[i]) > mayor:
            mayor = int(altura[i])
        if int(altura[i]) < menor:
            menor = int(altura[i])
    print(mayor - menor)
