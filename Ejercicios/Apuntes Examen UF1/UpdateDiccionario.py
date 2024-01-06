casos = int(input())
diccionario = {}
diccionario["x"] = {}
for _ in range(casos):
    nombre = input()
    fecha = input()
    diccionario["y"] = {nombre: fecha}
    diccionario["x"].update(diccionario["y"])
peticion = input()
print("{",end="")
for i, j in diccionario["x"].items():
    if i != nombre:
        print(f"{i}={j}", end=", ")
    if i == nombre:
        print(f"{i}={j}", end="")
print("}")
print(diccionario["x"][peticion])