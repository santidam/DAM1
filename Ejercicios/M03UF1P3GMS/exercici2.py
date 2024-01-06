import random # Importamos random para trabajar cn números aleatorios
numero = int(input("Introduce un número entre 10 y 50: ")) # Introcimos input con datos del rango requerido
lista = [] #Establecemos la lista con la que trabajaremos
suma = 0 # Creamos variable fuera de bucle para sumatoria de valores
apariciones = 0 # Variable para determinar la cantidad de veces que se repite un numero de la lista
masApariciones = 0 # Variable para determinar el número con más repeticiones
while numero <10 or numero > 50: #Mientras el usuario no introduzca un digito dentro del rango establecido, le volveremos a preguntar el digito
    numero = int(input("Error, introduce un numero entre 10 y 50: "))
for i in range(numero): # Con el  número introducido dentro del rango, generamos esa cantidad de números aleatorios
    n = random.randint(1,4)
    lista.append(n) # Añadimos a la lista los números aleatorios
    suma += n # Sumamos cada número aleatorio generado
for j in range(1, 5): # Contruimos el bucle para determinar la cantidad de veces que se repiten los números en lista, que son entre 1 y 4
    if lista.count(j) > apariciones: # Si procede reemplazamos cada vez con el número con mas repeticiones
        apariciones = lista.count(j) #Reemplazamos con el valor con mas repeticiones
        masApariciones = j # Determinamos que númro es el que más se repite
for k in lista: # Imprimimos en pantalla los numeros dentro de la lista
    print(k, end=" ")
print(f"\n" # Imprimimos los datos generados
      f"El numero que ha salido mas veces es el {masApariciones} con {apariciones} apariciones.\n"
      f"La media de los números es: {suma/numero}")
