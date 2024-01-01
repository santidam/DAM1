casos = int(input())
for i in range(casos):
    horaHuevo = input().split(" ")
    horaHuevoInicio = horaHuevo[0].split(":")
    huevoHoras = int(horaHuevoInicio[0])
    huevoMinutos = int(horaHuevoInicio[1])
    horaHuevoHorario = horaHuevo[1]  # HUEVO AM O PM
    tiempoHuevo = huevoHoras * 60 + huevoMinutos

    horaGolpe = input().split(" ")
    horaGolpeTiempo = horaGolpe[0].split(":")
    golpeHoras = int(horaGolpeTiempo[0])
    golpeMinutos = int(horaGolpeTiempo[1])
    horaGolpeHorario = horaGolpe[1]  # GOlPE AM O PM
    tiempoGolpe = golpeHoras * 60 + golpeMinutos

    tiempoMayonesa = input().split(":")  # DURACION GOLPE
    mayonesaHoras = int(tiempoMayonesa[0])
    mayonesaMinutos = int(tiempoMayonesa[1])
    duracionGolpe = mayonesaHoras * 60 + mayonesaMinutos

    duracion = 0
    if horaHuevoHorario == horaGolpeHorario:
        duracion = tiempoGolpe - tiempoHuevo
        if duracion < duracionGolpe:
            print("NO")
        else:
            print("SI")
    else:
        tiempoGolpe += 720
        duracion = tiempoGolpe - tiempoHuevo
        if duracion < duracionGolpe:
            print("NO")
        else:
            print("SI")
