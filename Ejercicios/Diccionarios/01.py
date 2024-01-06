# Diccionarios: lista en que el contenido no está determinado por su posición, sino por
# Su clave única
pokemon = {} # Creacion de diccionario
pokemon["pikachu"] = 345
pokemon["charmander"] = 66
pokemon["boby"] = 266
print(pokemon)
usuario = input("Que pokemon eliges: ")
if usuario in pokemon:
    print(pokemon[usuario])
else:
    print("No tengo mascota con ese nombre")
# Para imprimir elementos dentro deldiccionario:
for poke in pokemon:
    # Imprime los elementos y su contenido de biblioteca
    print(poke, pokemon[poke])

# imprimir valores de los elementos:
for valor in pokemon.values():
    print(valor)
mascotas = {}
mascotas["boby"] = {"come":266, "bebe:":"agua", "duerme": 18}
mascotas["pipo"] = {"come":25, "bebe:":"zumos", "duerme": 8}
mascotas["lola"] = {"come":123, "bebe:":"agua", "duerme": 12}
print(mascotas)
print(mascotas["pipo"]["duerme"])

