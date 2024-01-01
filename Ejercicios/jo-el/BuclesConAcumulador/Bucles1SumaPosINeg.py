numeros = 1
positivos = 0
negativos = 0
while numeros != 0:
    numeros = int(input())
    if numeros > 0:
        positivos += 1
    elif numeros < 0:
        negativos += 1
if positivos == negativos:
    print("IGUALS")
elif positivos > negativos:
    print("POSITIUS")
else:
    print("NEGATIUS")
