casos = int(input())
suma = 0
pisos = 0
aux = 0
for i in range(casos):
    cartas = int(input("C"))
    if cartas <= 2:
        print(f"{cartas // 2} {cartas % 2}")
    for j in range(2, cartas, 3):
        suma += j
        aux = suma
        pisos += 1
        resto = cartas - suma
        # print(suma)
        if cartas // suma == 1 and resto < j + 3:
            print(f"{pisos} {resto}")
        elif cartas / suma >= 2 and cartas / suma <= 4 and resto < j + 3:
            print(f"{pisos} {resto}")
    suma = 0
    resto = 0
    pisos = 0
