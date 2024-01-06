casos = int(input())
for _ in range(casos):
    frase = input()
    frase2 = []
    vocales = "aeiou"
    ganadora = ""
    repeticiones = [0] * len(vocales)
    repeticionMaxima = 0
    for caracteres in frase:
        if caracteres in vocales:
            indice = vocales.index(caracteres)
            repeticiones[indice] += 1
    for i in range(len(vocales)):
        if repeticiones[i] > repeticionMaxima:
            repeticionMaxima = repeticiones[i]
            ganadora = vocales[i]
    print(f"Vocal guanyadora: {ganadora}")