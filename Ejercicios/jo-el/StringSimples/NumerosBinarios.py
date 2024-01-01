casos = int(input())
for _ in range(casos):
    numeros = input().split()
    numero1 = int(numeros[0])
    numero2 = int(numeros[2])
    operacion = numeros[1]
    binario = []
    if operacion == "+":
        resultado = numero1 + numero2
        if resultado == 0:
            binario.append(resultado)
        while resultado != 0:
            binario.append(resultado % 2)
            resultado = resultado // 2
    elif operacion == "-":
        resultado = numero1 - numero2
        if resultado == 0:
            binario.append(resultado)
        while resultado != 0:
            binario.append(resultado % 2)
            resultado = resultado // 2
    binario.reverse()
    for i in range(len(binario)):
        print(int(binario[i]), end="")
    print()
