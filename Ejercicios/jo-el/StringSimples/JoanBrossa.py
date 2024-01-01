casos = int(input())
for _ in range(casos):
    frase = input()
    frase2 = []
    vocales = "aeiou"
    ganadora = ""
    repeticiones = 0
    for vocales in frase:
        if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o":
            frase2.append(vocales)
    for letras in frase2:
        if frase2.count(letras) > repeticiones:
            repeticiones = frase2.count(letras)
            ganadora = letras
    print(f"Vocal guanyadora: {ganadora}")
