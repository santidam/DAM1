#7. [1,5 punts] El director d'una escola està organitzant un viatge d'estudis,
#i requereix determinar quant ha de cobrar a cada alumne i quant ha de
#pagar a la companyia de viatges pel servei.
#La manera de cobrar és la següent: si són 100 alumnes o més, el cost per
#cada alumne és de 65 euros; de 50 a 99 alumnes, el cost és de 70 euros,
#de 30 a 49, de 95 euros, i si són menys de 30, el cost de la renda de
#l'autobús és de 4000 euros, sense importar el nombre d'alumnes.
#Feu un programa que demani el número d’alumnes i que permeti
#determinar el pagament a la companyia d'autobusos i el que ha de pagar
#cada alumne pel viatge.

alumnos = int(input("Introduce la cantidad de alumnos: "))  # Construimos la primera varibale que será un número entero introducido por el usuario, está será el número de alumnos.
autobus = 4000  # Creamos otra variable, que es el valor del precio del autobus, en este caso, 4000.

if alumnos >= 100: # Construimos la primera sentencia alternativa, con un comparador de operacion ">="
    print("Cada alumno debe pagar 65 euros")    # Si se cumple la sentencia introducida imprimimos lo que pagará cada alumno
    print("Total a pagar a la compañia de viajes: ", alumnos * 65) # Y si se cumple también le daremos al usuario el coste total del viaje
elif alumnos >= 50 and alumnos <= 99: # En el caso de que no se cumpla la sentencia anterior, establecemos esta para el rango 50 <= alumnos <= 99, usamos el operador logico "and", esto determinará el cumplimiento de ambas comparaciones para que la sentencia se "True".
    print("Cada alumno debe pagar 70 euros") # Imprimimos en pantalla lo que paga cada alumno en este rango, que es 70
    print("Total a pagar a la compañia de viajes: ", alumnos * 70)  # Y tambien el total a pagar a la compañia de viajes, imprimiendo la operación alumons x cuota.
elif alumnos >= 30 and alumnos <= 49:   # Desarrollamos esta tercera sentencia para el rango, 30 <= alumnos <= 49, nuevamente usamos el operdor lógico "and"
    print("Cada alumno debe pagar 95 euros")    # Imprimimos la cuota a pagar en este rango por cada alumno
    print("Total a pagar a la compañia de viajes: ", alumnos * 95)  # Y la cantidad a pagar en la compañia de viajes, volvemos a operar almunos * cuota, en este caso 95
elif alumnos < 30:  # Establecemos la ultima sentencia para cuando la variable almunos introducida es <= 30
    print("Cada alumno debe pagar", autobus / alumnos)  # Imprimimos la cuota a pagar, en este caso a diferencia de las otras sentencias, la cuota fija para este rango es 4.000 a pagar entre el total de almunos, apara ello imprimimos la variable almunos / autobus que reflejará la cuota a pagar
    print("Total a pagar a la compañia de viajes", autobus) # Por último imprimimos la cantidad  pagar, que en este rango <= 30, será de 4.000 siempre. Por ello escribimos el nombre de la variable "autobus" escriya ya previamente.
