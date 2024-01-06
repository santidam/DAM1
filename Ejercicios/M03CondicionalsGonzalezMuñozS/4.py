# 4. [0,5 punts] Una botiga de música ven partitures de piano, guitarra,
# bateria i saxo. De cada instrument té un número determinat de partitures:
#
# Instrument Nº de partitures
# Guitarra 696
# Piano 718
# Bateria 256
# Saxo 310
# Demana a l’usuari de quin instrument vol partitures i mostra-li quantes
# hi ha de l’instrument escollit. Si posa un instrument que no sigui a la llista
# ha de donar missatge d’error.

guitarra = 696  # En primer lugar, ingresamos las variables guitarra, piano, bateria, saxo con su determinado número de partituras, para asociarlas
piano = 718     # al valor que les corresponde de partituras.
bateria = 256
saxo = 310
print("Programa informativo para partituras de piano, guitarra, bateria y saxo: ") # Usamos un print para iniciar el programa en la interfaz del usuario
instrumento = input("Introduce el nombre del intrumento: ")  # Creamos la variable "intrumento, introducida por el usuario
if instrumento == "piano": # Construimos la primera condicional, si la variable instrumento introducida por el usuario es == piano,  imprimimos
    print("El instrumento seleccionado dispone de: ", piano, "partituras") # el número de partituras de la variable piano, para ello la ponemos fuera de las comillas en el print.
elif instrumento == "guitarra" : # Introducimoms un "elif" para la siguiente condicinal,y al igual que en el caso anterior, si se satisface que el string introducido por el usuario cumple la igualdad "== guitarra", imprimimos
        print("El instrumento seleccionado dispone de: ", guitarra, "partituras")   # las partituas de la variable guitarra
elif instrumento == "bateria" : # Realizamos el mismo proceso anterior
        print("El instrumento seleccionado dispone de: ", bateria, "partituras") # Si es correcto, imprimimos en pantalla las partiruas
elif instrumento == "saxo" : #Realizamos los mismos procesos anteriores
        print("El instrumento seleccionado dispone de: ", saxo, "partituras") # imprimimos en pantalla
else:  # En caso de que no se cumplan, niguna de las condiciones anteriores, y el usuario no a introducido ningún string valido, en este "else" invalidaremos la respuesta del usuario
    print("Error, nombre introducido no registrado en base de datos") # Imprimimos el mensaje de error
    print("Introduce piano, guitarra, bateria o saxo") # Le sugerimos al usuario el comando a introducir.