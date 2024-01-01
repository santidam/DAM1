casos = int(input())
for _ in range(casos):
    palabra = input()
    contador = 0
    for letra in palabra:
        if letra.islower():
            contador += 1
    print(contador)
