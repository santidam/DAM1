casos = int(input())
for _ in range(casos):
    palabra1 = input()
    palabra2 = input()
    letras = 0
    for i in range(len(palabra1)):
        if i < len(palabra1) and i < len(palabra2):
            if palabra1[i] == palabra2[i]:
                letras += 1
    if len(palabra1) >= len(palabra2):
        if letras >= len(palabra1)/2:
            print("GRACIES WEBCASTELLER")
        else:
            print("WEBCASTELLER ESTA TRAVIESO HOY")
    if len(palabra2) > len(palabra1):
        if letras >= len(palabra2)/2:
            print("GRACIES WEBCASTELLER")
        else:
            print("WEBCASTELLER ESTA TRAVIESO HOY")
