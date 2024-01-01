lista = []
k = int(input())
elementos = input()
numero = 0
n = elementos.split(" ")
for _ in range(k):
    lista.append(float(n[_]) * 100)
    if _ == k - 1:
        for i in range(k):
            print(lista[i], "%", sep="", end=" ")
