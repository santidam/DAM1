import random #Importamos random para trabajar con números aleatorios
# Escriu el codi que generi 30 números aleatoris entre 0 i 29 i els desi en una llista. Ha de
# mostrar-los tots i finalment indicar quins números han coincidit amb la seva posició. Si cap
# número coincideix amb la seva posició ho haurà d'indicar.

lista = [] # Creamos lista
contador = -1 # Añadimos contadores
ninguno = 0 # Variable para indicar la cantidad de coincidencias
for i in range(30): # Creamos bucle para generar números random
    numero = random.randint(0,29)
    lista.append(numero) # Añadimos números random generados a la lista
for j in lista: # Imprimimos los elementos de la lista
    print(j, end=" ")
for j in lista: # Construimos este bucle para determinar junto con el contador
    contador += 1 # en qué casos los elementos de la lista coinciden con su indice
    if j == contador: # If j == lista[j], habría sido una mejor opciopn
        print(f"\n"
              f"El número {j} está en la posición {contador}")
        ninguno += 1 # en caso de que exista alguna coincidencia añadimos uno a la variable
if ninguno == 0: # Determinamos el caso en el que no exista ninguna coincidencia
    print("\n"
          "Ningún número ha coincido con su posición")
