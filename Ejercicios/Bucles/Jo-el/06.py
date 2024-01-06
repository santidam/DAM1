k = 1
p = 100000
g = -100000
while k != 0:
    k = int(input())
    if k > g and k != 0:
        g = k
    elif k < p and k != 0:
        p = k
print(g , p)