#1)
print("Exercici 1"
      "apartat a")
numeros = [6, 1, 2, 3, 8, 1, 0, 3, 0, 0, 4, 5, 7]
#a)
print(f"La llista de numeros: {numeros}")
#b)
print("apartat b")
print(f"La llista té: {len(numeros)} elements")
#c)
print("apartat c")
print(f"A la posició 4 de la llista hi ha: {numeros[3]}")
#d)
numeros.append(9)
#e)
numeros.insert(1,4)
#f)
print("apartat f")
print(f"La llista numeros:  {numeros}")
#g)
numeros.remove(6)
#H)
print("apartat h")
print(f"La llista numeros:  {numeros}")
#i)
print(f"El darrer element de la llista es {numeros[-1]}")
#j)

print()
suma = 0
for i in numeros:
    print(i)
    suma += i
print()
print(f"la suma dels elements de la llista és: {suma}")
#k)
num = int(input("Introduce un número: "))
if num in numeros:
    print(num, "está en la lista")
elif num not in numeros:
    print(f"{num} no está en la lista")

#l)
numeros.append(6)
#m)
print(f"La llista de numeros: {numeros}")
#n)
n = int(input("Introduce un numero"))
print(f"el numero {n} apareix {numeros.count(n)} veces")
#o)
print("apartat o")
n2 = int(input("Introduce un numero"))
if n2 not in numeros:
    print(f"{n2} no está en la lista")
elif n2 in numeros:

    print(f"el numero {n2} esta en la posición {numeros.index(n2)}")
#p)
print("apartat p")
numeros.reverse()
print(f"La llista invertida: {numeros}")
#q)
print("apartat q")
numeros.sort()
print(f"la llista ordenada : {numeros}")




