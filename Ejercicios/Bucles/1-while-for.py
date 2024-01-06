import random
aleatorio = random.randint(-50,50)
while aleatorio >=0: # cuando el nnumero generado es negativo se acaba el bucle, mientras se cumpla la condicion el bucle continua
    print(aleatorio)
    aleatorio =  random.randint(-50,50) # importante, esta sentencia para generar una nueva variable "aleatorio

for numero in range(10, 20, 3):     # Recorer frases, listas de datos, rango de números.
    print(numero)   #Imprimimos la variable creada en for, en este caso "numero", el tercer valor en rango determina