casos = int(input())
for _ in range(casos):
    entrada = int(input())
    datos = input()
    lista = datos.split(" ")
    folio = input()
    contador = 0
    if folio in lista:
        print(lista.index(folio))
    else:
        print(-1)

