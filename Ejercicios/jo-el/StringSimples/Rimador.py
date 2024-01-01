casos = int(input())
for _ in range(casos):
    frase = input().split(", ")
    frase1 = frase[0].split(" ")
    frase2 = frase[1].split(" ")
    rima = ""
    for i in range(1, len(frase1[-1]) + 1):
        if i <= len(frase2):
            if frase1[-i] == frase2[-i] and i == 1:
                rima += frase1[-i]
            elif len(rima) > 0:
                if frase1[-i] == frase2[-i]:
                    rima += frase1[-i]

    if len(rima) == 0:
        print("#")
    else:
        print(rima)
