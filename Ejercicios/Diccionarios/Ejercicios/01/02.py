#Escriu un programa que guardi en un diccionari els preus dels productes de
#la taula, pregunti a l’usuari per un producte, la quantitat i mostri per
#pantalla el total del preu de la seva compra. Si el producte no està al
#diccionari ha de mostrar un missatge indicant-ho.

diccionario = {}
diccionario["refresc"] = 1.25
diccionario["apertiu"] = 0.9
diccionario["pastisset"] = 1.05
diccionario["galetes"] = 1.35
diccionario["suc"] = 0.95
producto = input("Introduce el producto que quieres añadir: ")
cantidad = int(input("Cuantas unidades quieres: "))
if producto in diccionario:
    print(f"El total de la compra es :{diccionario[producto] * cantidad} €")
else:
    print("EL producto que has introducido no se encuentra en la lista")
