# :1)calcula la altura de alguien en metros y centrimetros con pies y polzadas como dato de entrada
print("Calcula la altura en metros y centímetros entregando pies y pulgadas")
pies = float(input("ingresa los pies: "))
pulgadas = float(input("ingresa las pulgadas: "))
e1 = pulgadas * 25.4  # pulgadas en mm
e12 = pies * 25.4 * 12  # pies en mm
e13 = (e1 + e12) // 1000  # metros
e14 = ((e1 + e12) % 1000) / 10  # centimetros
print("la altura es de: ", e13, "metros, ", e14, "centimetros")

# 2)Programa de asitencia a fiesta, con lista de compra, cada asitente bebe una lata de cocacola
# come 2 sandwich de nutela, las latas se venden en àchs de y, el pan bimbo en bolsas de 20
# con una nutela haces 15 sandwich.
# -cantidad de asistentes a fiesta - lista de la compra - cuantas latas y panes han sobrado

print("Programa para crear evento: ")
asistentes = int(input("ingresa la cantidad de asistentes a la fiesta: "))
sandwich = asistentes * 2
latas = asistentes
pack = (latas // 6) + 1
pan = sandwich * 2
bolsa = (pan // 20) + 1
nutela = (sandwich // 15) + 1
ppack = pack * 5
pbolsa = bolsa * 1.5
pnutela = nutela * 2.5
presupuesto = ppack + pbolsa + pnutela
print("Lista de la compra:")
print(pack, " packs de coca cola: ", ppack, "euros")
print(bolsa, " bolsas de pan de molde: ", pbolsa, "euros")
print(nutela, " potes de nutela: ", pnutela, "euros")
print("Total: ", presupuesto, "euros")
xlatas = pack * 6 - latas
xpan = bolsa * 20 - pan
xnutela = (nutela * 15 - sandwich) / 15
print("Sobran: ", xlatas, "latas de coca cola")
print("Sobran: ", xpan, "rebanadas de pan")
print("sobran: ", xnutela, "botes de nutella")

#: 3) Dissenyeu un programa que, donat un nombre enter pel teclat que representa
# un import en cèntims d’euro, ho descompongui en monedes. Així doncs, minimitzant
# el nombre de monedes ha de retornar el nombre de monedes de dos euros, un euro,
# cinquanta cèntims, vint cèntims, deu cèntims, cinc cèntims, dos cèntims i un cèntim
# necessaris per representar l'import.

print("Programa de descomposición de monedas: ")
centimos = int(input("Ingresa un valor para centimos: "))
xeuros = centimos // 100
xcentimos = centimos % 100
euros2 = xeuros // 2
euros1 = xeuros % 2
cent50 = xcentimos // 50
cent20 = (xcentimos % 50) // 20
cent10 = ((xcentimos % 50) % 20) // 10
cent5 = (((xcentimos % 50) % 20) % 10) // 5
cent2 = ((((xcentimos % 50) % 20) % 10) % 5) // 2
cent1 = ((((xcentimos % 50) % 20) % 10) % 5) % 2
print("La cantidad de monedas que tienes es:")
print(euros2, "monedas de 2 euros")
print(euros1, "monedas de 1 euro")
print(cent50, "monedas de 50 centimos")
print(cent20, "monedas de 20 centimos")
print(cent10, "monedas de 10 centimos")
print(cent5, "monedas de 5 centimos")
print(cent2, "monedas de 2 centimos")
print(cent1, "monedas de 1 centimo")

# 4) Crea un programa que para valores iguales a 0 o multiplos de 180 responda ok, para el resto "bronca"

print("Iniciando verificación de aire: ")
grados1 = int(input("Ingrese valor de grados: "))
grados2 = int(input("Ingrese valor de grados: "))
grados3 = int(input("Ingrese valor de grados: "))
grados4 = int(input("Ingrese valor de grados: "))

if grados1 == 0 or grados1 % 180 == 0:
    print("Aire 1 : OK")
else:
    print("Aire 1 : Bronca")
if grados2 == 0 or grados2 % 180 == 0:
    print("Aire 2 : OK")
else:
    print("Aire 2 : Bronca")
if grados3 == 0 or grados3 % 180 == 0:
    print("Aire 3 : OK")
else:
    print("Aire 3 : Bronca")
if grados4 == 0 or grados4 % 180 == 0:
    print("Aire 4 : OK")
else:
    print("Aire 4 : Bronca")
