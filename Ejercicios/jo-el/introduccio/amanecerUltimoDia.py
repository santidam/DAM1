segundos = int(input("Introduce la cantida de segundos: "))
horas = segundos / 3600
dia = int((horas // 24) + 1)
momento = horas // 12
print(momento)

if segundos <= 0 or segundos > 100000000:
    print("Error, introduce un numero entre 1 y 100000000")

else:
    if momento % 2 != 0:
        print(f"noche del día {dia}")
    else:
        print(f"mañana del día {dia}")
