casos = int(input())
for _ in range(casos):
    lista = input().split(" ")
    cantidadMiradas = int(input())
    horaMiradas = input().split(" ")
    shitNivel = 0
    lista2 = []
    listaJuegos = ["HollowKnight", "DarkSouls", "Zelda"]
    for i in range(len(horaMiradas)):
        horaMiradas[i] = int(horaMiradas[i])
    for j in range(15, 21):
        if j in horaMiradas:
            lista2.append(j)
        else:
            lista2.append(0)
    indice = 0
    for i in range(6):
        if lista2[i] != 0:
            if lista[i] in listaJuegos and shitNivel <= 1:
                shitNivel = 1
            elif lista[i] == "LoL":
                shitNivel = 2
    print(f"Nivell de Shitlist: {shitNivel}")