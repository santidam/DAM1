x = input("Introduce una frase: ")
contador = 0
for i in x:
    if contador == 0 or contador % 2 == 0:
        print(i, end="")
        contador += 1
    else:
        contador += 1