# dicc = {"pepe":{"a": 1, "b": 1}, "papa":{"a": 2, "b": 2}}
# for x, y in dicc.items():
#     for i, j in y.items():
#         print(f"{i}{j} ", end="")

# comanda = "listllibres"
# comandaFinal = comanda.split("-")
# print(len(comandaFinal))

def prueba(numero):
    for i in range(numero):
        print(i)
# prueba()
# dicc["pepe"] = {[]}
# print(len(dicc))
# print(f"Esto es\n Una prueba \n veremos \n si \n salta")
# print(f"prueba")
diccIncidiencias = {}
diccIncidiencias["pepe"] = [{"codigo": "123", "fecha prestamo": "2024/01/30", "fecha devolucion": "2024/02/13", "fecha entrega": "2024/02/20"}]
diccIncidiencias["pepe"].append({"codigo": "1234", "fecha prestamo": "2024/01/30", "fecha devolucion": "2024/02/13", "fecha entrega": "2024/02/20"})
diccIncidiencias["prueba"] = [{"codigo": "123", "fecha prestamo": "2024/01/30", "fecha devolucion": "2024/02/13", "fecha entrega": "2024/02/20"}]
print(diccIncidiencias)

# for x in diccIncidiencias["pepe"]:
#     print(x)
    # print("Llibre:", 001 Data Inici Préstec: 2023-03-01 Data Fi: 2023-03-16 Data Retorn: 2023-03-31)
print("El alumno tiene", len(diccIncidiencias["prueba"]))
for i in range(len(diccIncidiencias["pepe"])):
    print(diccIncidiencias["pepe"][i]["codigo"])