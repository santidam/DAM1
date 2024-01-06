#L’empresa Digues Patata Exprés s’encarrega de fer patates fregides a totes hores i
#entregar-les a domicili. Cada dia camions i camions de patates van arribant i descarregant.
#Escriu un programa que les sumi totes

casos = int(input("Introduce la cantidad de casos a considerar: ")) #Primera variable para determinar la cantidad de casos a considerar
if casos < 0:
    print(f"Error, has introducido una cantidad de casos negativa")
elif casos == 0:
    print("Has introducido 0 casos, cerrando programa")
else:
    for i in range(casos): # Creamos un bucle for con la cantidad de intentos introducidos en la variable anterior
        camiones = input("Introduce la cantidad de camiones, y patatas en cada carga: ") # En esta variable el usuario ingresará: los camiones y la cantidad de patatas
        patatas = camiones.split(" ") # Con la variable camiones creamos una lista con cada elemento separado por un espacio
        suma = 0 # Variable para sumatoria de patatas
        if int(patatas[0]) > 0: # Protegemos codigo para los casos en los que la cantidad de camiones pueda ser menor a 0
            for j in range(1,int(len(patatas))): # Bucle for en el que determinaremos la cantidad de sumas de patatas
                if int(patatas[j]) > 0:
                    suma += int(patatas[j]) # Sumamos las patatas
                else:
                    print(f"Error, la carga introducida: {patatas[j]} es negativa , no se tomará en cuenta")
            print(suma) # Imprimimos la sumatoria
        else: # Error cuando la cantidad de camiones introducida por el usuario es 0
            print("Error has introducido una cantidad de camiones menor a 1")




