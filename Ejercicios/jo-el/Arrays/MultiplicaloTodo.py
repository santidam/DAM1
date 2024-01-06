k = int(input())
for i in range(k):
    cantidad = int(input())
    numeros = input()
    n = numeros.split(" ")
    mult = int(input())
    for j in range(len(n)):
        n[j] = int(n[j]) * mult
    for x in n:
        print(x, end=" ")
    print()
