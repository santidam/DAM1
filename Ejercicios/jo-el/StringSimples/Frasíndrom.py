frase = ""
bucle = True
while bucle == True:
    frase = input().split(" ")
    capicua = 0
    if frase[0] == ".":
        bucle = False
    else:
        for i in range(len(frase)):
            if len(frase) % 2 == 0 and i < len(frase)/2:
                if frase[i] == frase[-i-1]:
                    capicua += 1
            elif len(frase) % 2 != 0 and i < (len(frase)-1)/2:
                if frase[i] == frase[-i-1]:
                    capicua += 1
        if len(frase) % 2 == 0:
            if capicua == len(frase)/2:
                print("SI")
            else:
                print("NO")
        elif len(frase) % 2 != 0 and len(frase) != 1:
            if capicua == (len(frase) - 1) / 2:
                print("SI")
            else:
                print("NO")
        elif len(frase) == 1:
            print("SI")
