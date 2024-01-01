k = int(input())
while k != 0:
    numero = int(input())
    p = 0
    s = 0
    for i in range(1, numero+1):
        if i % 2 == 0:
            p += i
        elif i % 2 != 0:
            s += i
    print("PARELLS:", p, "SENARS:", s)
    k -= 1
