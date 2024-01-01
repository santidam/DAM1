casos = int(input())
for _ in range(casos):
    cartas = input()
    lista = cartas.split(" ")
    lista.sort
    lista2 = []
    escalera = False
    escaleraReal = False
    for i in range(7):
        int(lista[i])
        if int(lista[i]) not in lista2:
            lista2.append(int(lista[i]))
    lista2.sort()
    if len(lista2) >= 5:
        for j in range(len(lista2) - 1, -1, -1):
            if j >= 4:
                if int(lista2[j]) == int(lista2[j-1]) + 1 and int(lista2[j]) == int(lista2[j-2]) + 2 and int(lista2[j]) == int(lista2[j-3]) + 3 and int(lista2[j]) == int(lista2[j-4]) + 4:
                    escalera = True
            elif j == 0:
                if int(lista2[len(lista2)-1]) == int(lista2[len(lista2)-2]) + 1 and int(lista2[len(lista2)-1]) == int(lista2[len(lista2)-3]) + 2 and int(lista2[len(lista2)-1]) == int(lista2[len(lista2)-4]) + 3 and int(lista2[j]) == 1 and int(lista2[len(lista2)-1]) == 13:
                    escaleraReal = True
    if escaleraReal == False and escalera == False:
        print("NO")
    else:
        if escaleraReal == True:
            print("ESCALA REIAL")
        elif escalera == True:
            print("ESCALA")
