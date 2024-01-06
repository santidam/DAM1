# 5. [1,5 punts] Joc pedra-paper-tisores: Demana a l’usuari que indiqui una
# de les tres opcions (pedra, paper o tisores). Si el que introdueix l’usuari no
# és correcte ha de mostrar el missatge de que no és correcte i acabar el
# programa. En cas de que sigui correcte, demanar un altra vegada una altra
# opció i comprovar igualment que sigui correcte, com en el primer cas.
# En cas de que siguin les dues correctes indicar si ha guanyat el primer
# jugador, el segon o si hi ha empat.


print("Iniciando juego de piedra, papel, tijera ")  # Imprimimos en la pantalla el inicio del programa.

jugada = input("Jugador 1 introduce piedra, papel o tijera: ")  # Creamos la primera variable "jugada" introducida por el usuario

if jugada == "piedra" or jugada == "papel" or jugada == "tijera": # Si la variable jugada introducida por el usuario cumple con las igualdades de los string que hemos establecido,
    print("OK") # Confirmamos la varibale introducida por el usiario
    jugada2 = input("Jugador 2 introduce piedra, papel o tijera: ") # Y ingresamos el siguiente input para establecer la variable jugada2
    if jugada2 == "piedra" or jugada2 == "papel" or jugada2 == "tijera": # Si la variable jugada2 introducida por el usuario cumple con las igualdades dadas, compo en el if anterior, confirmamos
        print("OK") # Imprimimos la confirmación
        if jugada == jugada2: # Anidado al if anterior establecemos este nuevo "if", y establecemos los casos de victorias y derrotas
            print("Empate") # Si las jugadas introducidas por jugada y jugada2 son iguales, entonces imprimimos empate
        elif jugada == "piedra" and jugada2 == "tijera": # En los siguientes, 3 "elif" determinaremos los casos en los que gana el jugador 1
            print("Gana el jugador 1")  # imprimimos la victoria del jugador 1 dada la condición anterior
        elif jugada == "papel" and jugada2 == "piedra": # Establecemos otra condición para el jugador uno
            print("Gana el jugador 1")  # Realizamos la impresión en pantalla de la victoria
        elif jugada == "tijera" and jugada2 == "papel":  # Creamos la tercera y ultima condición de victoria del jugador 1
             print("Gana el jugador 1") # imprimimos en pantalla
        else:   # En este else, determinamos que para el resto de viariables introducidas por el jugador1 y jugador2 ganará el jugador 2.
            print("Gana el jugador 2") # Imprimimos en pantalla
    else:   # Introducimos este else, que está ligado el cumplimiento del if en el que confirmamos que los string para jugada2 escritos por el usuario en la terminal
        print("La jugada introducida no es correcta")   # son correctos, si no coincidieran, se imprimiría en pantalla que la jugada es incorrecta y el programa terminaría.
else: # Acabamos con este else, que esta ligado a la confirmación de los datos ingresados para jugada1, para la cual, si los string ingresados por el usuario no
    print("La jugada introducida no es correcta") # fuesen correctos, el programa terminaría en el primer error del usuario. Para terminar cerramos con un print, avisandole al suaurio que los datos introducidos no son correctos.
     # En este ejercicio, se tiene que cuidar muy bien la anidación o "identation" de cada sentencia alternativa introducida, apra así cuidar de que el programa tenga las salidas adecuadas en caso de
     # que el usuario cometa errores a la hora de introducir los comandos en la terminal.