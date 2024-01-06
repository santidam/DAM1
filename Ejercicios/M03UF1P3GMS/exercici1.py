#1)Crear un programa que afegeixi números a una llista fins que introduïm un número negatiu.
#Mostra-la. A continuació s’ha de crear una nova llista igual que l’anterior però eliminant els
#números duplicats. Mostra aquesta segona llista per comprovar que hem eliminat els
#duplicats

lista1 = [] # Construimos listas
lista2 = []
numeros = 0 # Creamos variable para iiciar bucle
while numeros >= 0: # Si cumple la condicion el bucle continuará
    numeros = int(input("Intrduce un número positivo para añadir, o un negativo para salir: "))
    if numeros >= 0: # Si el número es mayor o igual a 0 lo añadimos a la lista
        lista1.append(numeros)
print("Lista de números")
for i in lista1: # Imprimimos la primera lista
    print(i, end=" ")
    if i not in lista2: # Si los valores de la primera lista no se encuentran en la segunda lista que hemos creado
        lista2.append(i) # Añadiremos esos valores a la lista 2
print(F"\n"
      F"Lista de números sin repeticiones") # Imprimimos un salto de línea
for j in lista2: # Último bucle para producir los números de la lista 2
    print(j, end=" ")