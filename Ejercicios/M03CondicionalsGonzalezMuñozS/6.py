#[1 punt] Fes un programa que demani les hores que té una Unitat
#Formativa, les faltes d'assistència que s'han fet (les justificades i les no
#justificades) i digui si es té dret a l'avaluació o no.
#Recorda que, com a màxim, es poden fer un 10% de faltes injustificades i
#un 20% de justificades + no justificades.

unidad = int(input("Ingresa la cantidad de horas que tiene la unidad formativa: ")) # Introducimos la primera variable del usuario, usamos int. para guardar el valor ingresado por el usuario como número entero. Esta variable corresponderá a la cantidad de horas formativas.
faltasjus = int(input("Ingresa la cantidad de faltas justificadas: "))  # Creamos la segunda variable que determinará las faltas injustificadas, y al igual que la variable anterior usamos int.
faltasin = int(input("Ingresa  la cantidad de faltas injustificadas: "))    # En esta última variable solicitamos al usuario, las horas injustificadas, tambien en enteros
faltas = faltasjus + faltasin # Por ultimo establecemos una variable final con la suma de las faltas justificadas e injustificadas
if faltasjus > unidad * 0.2 or faltasin > unidad * 0.1 or faltas > unidad  * 0.2:   # Creamos una sentencia alternativa con las condiciones adecuadas para que se cumplan los estandares evaluación, que
    print("NO ")    # pedido, en la sentencia, usamos el operador lógico "or" para determinar que si se cumple cualquiera de las tres condiciones establecidas, se imprima en pantalla "NO".
else:
    print("SI")     # si no se cumple ninguna de las condiciones anteriores para las variables que el usuario ha ingresado, signfica que puede ser evaluado, para ello imprimimos "SI".