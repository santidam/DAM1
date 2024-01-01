casos = int(input())
diccionario = {}
diccionario["x"] = {}
for _ in range(casos):
    nombre = input()
    fecha = input()
    diccionario["y"] = {nombre: fecha}
    diccionario["x"].update(diccionario["y"])
peticion = input()
print(diccionario["x"])
print(diccionario["x"][peticion])
for i in diccionario["x"]:
    print([i], diccionario["x"][i])
print(diccionario["x"].keys())

for x, y in diccionario["x"].items():
    print(x, y, sep="=", end=", ")
