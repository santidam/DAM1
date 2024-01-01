k = int(input())
rondas = 0
asesino = 0
for i in range(k):
    datos = input()
    numeros = datos.split(" ")
    vida = int(numeros[0])
    daño = int(numeros[1])
    veneno = int(numeros[2])
    while vida > 0:
        vida -= daño
        asesino += 1
        if vida > 0:
            vida -= veneno
            asesino += 1
        rondas += 1
    if vida <= 0 and asesino % 2 != 0:
        print(f"RAMMUS {rondas}")
    elif vida <= 0 and asesino % 2 == 0:
        print(f"TWITCH {rondas}")
    rondas = 0
    asesino = 0
