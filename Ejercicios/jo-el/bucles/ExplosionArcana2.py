inicio = int(input())
vida = int(input())
veces = 0
daño = inicio
while vida > 0:
    vida -= daño
    daño += inicio
    veces += 1
print(veces)
