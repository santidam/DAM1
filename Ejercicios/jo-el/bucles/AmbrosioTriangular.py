suma = 0
casos = int(input())
suma2 = 0
for i in range(casos):
    altura = int(input())
    for j in range(1, altura + 1):
        suma += j
        if j <= altura - 1:

            suma2 += suma
        elif j == altura:
            print(suma + suma2)
            suma = 0
            suma2 = 0
