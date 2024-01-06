lista = []
k = 1
while k <=5:
    x = input("Introduce caracter: ")
    lista.append(x)
    k += 1
lista2 = lista
lista2.reverse()
print(f"lista: {lista}")
print(f"lista en reversa: {lista2}")
