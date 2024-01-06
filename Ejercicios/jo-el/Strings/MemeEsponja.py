casos = int(input())
for _ in range(casos):
    frase = input()
    frase2 = ""
    contador = 1
    for i in range(len(frase)):
        if frase[i] != " ":
            if contador % 2 == 0:
                frase2 += frase[i].upper()
                contador +=1
            else:
                frase2 += frase[i].lower()
                contador +=1
        elif frase[i] == " ":
            frase2 += " "
    print(frase2)