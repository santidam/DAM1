k = int(input())
while k != 0:
    numero = int(input())
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=" ")
    print()
    k -= 1
