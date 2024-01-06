# Escriu un programa que creï un diccionari simulant una cistella de la
# compra. El programa ha de preguntar l’article i el seu preu i afegir el parell
# al diccionari, fins que l’usuari decideixi acabar (Si l’usuari intenta posar dos
# articles amb el mateix nom s’ha de donar missatge d’error i tornar a
# demanar si es vol continuar o acabar).

diccionario = {}
salir = True
while salir == True:
    productos = input("Introduce un producto para la lista o salir para salir: ").lower()
    if productos == "salir":
        salir = False
    elif productos in diccionario:
        print("Error, la variable introducida ya está en la lista")
    else:
        precio = float(input("Introduce su precio: "))
        diccionario[productos] = precio
    suma = 0
for i in diccionario:
    print(i, diccionario[i])
    suma += diccionario[i]
print(f"Total: {suma}")
