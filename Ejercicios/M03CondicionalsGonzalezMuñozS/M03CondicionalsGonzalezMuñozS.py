#1. [0,5 punts] Escriu el codi necessari per demanar dos números enters a
#l’usuari entre 1 i 100. Guarda’ls a les variables num1 i num2. Mostra'ls per
#pantalla. Indica si num1 i num2 estan dins del rang demanat (entre 1 i
#100).

num1 = int(input("Introduce un número entero entre 1 y 100: "))
num2 = int(input("Introduce otro número entero entre 1 y 100: "))
print("El primer número introducido es: ", num1)
print("El segundo número introducido es: ", num2)
if num1 >= 1 and num1 <= 100:
    print("El primer número introducido está en el rango")
else:
    print("El primer número introducido no está en el rango")
if num2 >= 1 and num2 <= 100:
    print("El segundo número está en el rango")
else:
    print("El segundo número introducido no está en el rango")

# 2. [0,5 punts] Escriu el codi necessari que indiqui si la variable num2 és
# parell.

if num2 % 2 == 0:
    print("La segunda variable ", num2, "introducida es par")
else:
    print("La segunda variable ", num2, "introducida no es par")

# 3. [0,5 punts] Escriu el codi necessari que indiqui si num1 i num2 són
# imparells.

if num1 % 2 != 0:
    print("El primer número introducido: ", num1, "no es par")
if num2 % 2 != 0:
    print("El segundo número introducido: ", num2, "no es par")

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

guitarra = 696
piano = 718
bateria = 256
saxo = 310
print("Programa informativo para partituras de piano, guitarra, bateria y saxo: ")
instrumento = input("Introduce el nombre del intrumento: ")
if instrumento == "piano" :
    print("El instrumento seleccionado dispone de: ", piano, "partituras")
elif instrumento == "guitarra" :
        print("El instrumento seleccionado dispone de: ", guitarra, "partituras")
elif instrumento == "bateria" :
        print("El instrumento seleccionado dispone de: ", bateria, "partituras")
elif instrumento == "saxo" :
        print("El instrumento seleccionado dispone de: ", saxo, "partituras")
else:
    print("Error, nombre introducido no registrado en base de datos")
    print("Introduce piano, guitarra, bateria o saxo")
# 5. [1,5 punts] Joc pedra-paper-tisores: Demana a l’usuari que indiqui una
# de les tres opcions (pedra, paper o tisores). Si el que introdueix l’usuari no
# és correcte ha de mostrar el missatge de que no és correcte i acabar el
# programa. En cas de que sigui correcte, demanar un altra vegada una altra
# opció i comprovar igualment que sigui correcte, com en el primer cas.
# En cas de que siguin les dues correctes indicar si ha guanyat el primer
# jugador, el segon o si hi ha empat.
print("Iniciando juego de piedra, papel, tijeras :")
jugador1 = jugada
jugador2 = jugada2
x = jugador1 + jugador2
jugada = input("Jugador 1 introduce piedra, papel o tijeras: ")
if jugada == "piedra" or jugada == "papel" or jugada == "tijeras":
    jugada2 = input("Jugador 2 introduce otra jugada: ")
elif jugada2 == "piedra" or jugada2 == "papel" or jugada2 == "tijeras":
    print("Gana el jugador")
elif jugada + jugada2 
else:
     print("La jugada introducida no es correcta")



