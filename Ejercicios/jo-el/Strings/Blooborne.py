casos = int(input())
for _ in range(casos):
    frase = input()
    contador = 0
    for i in range(len(frase)):
        if i < len(frase) -1:
            if frase[i] == frase[i+1]:
                contador += 1
    if contador >= 1:
        print("SI")
    else:
        print("NO")