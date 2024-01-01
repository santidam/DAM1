
top = int(input())
torneo = int(input())
aux = top
if torneo == 0:
    print(top)
else:
    for i in range(torneo):
        aux //= 2
        if i == torneo - 1:
            print(aux)
