casos = int(input())
for _ in range(casos):
    lista = []
    cantidad = int(input())
    for __ in range(cantidad):
        elemento = input()
        if elemento not in lista:
            lista.append(elemento)
    print("[", end="")
    for i in lista:
        if i != lista[-1]:
            print(f"{i}, ", end="")
        else:
            print(f"{i}", end="")
    print("]")
