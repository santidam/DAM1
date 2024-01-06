k = 1
lista = []
media = 1
while k <= 5:
    notas = int(input())
    if notas < 0 or notas > 10:
        print("Las notas introducidas deben estar entre 0 y 10")
    else:
        lista.append(notas)
        media += notas
        lista.sort()
        k += 1
#for nota in lista:
print(f"Notas introducidas: {lista}\n"
      f"Nota media:  {media / len(lista)}\n"
      f"Numero menor: {lista[0]}\n"
      f"Numero mayor:  {lista[-1]}")