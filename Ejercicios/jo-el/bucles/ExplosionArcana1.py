inicio = int(input())
veces = int(input())
daño = 0
for i in range(1, veces + 1):
    daño += i * inicio
    if i == veces:
        print(daño)
