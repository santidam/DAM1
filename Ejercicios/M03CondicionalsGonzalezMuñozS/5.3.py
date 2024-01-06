# 5. [1,5 punts] Joc pedra-paper-tisores: Demana a l’usuari que indiqui una
# de les tres opcions (pedra, paper o tisores). Si el que introdueix l’usuari no
# és correcte ha de mostrar el missatge de que no és correcte i acabar el
# programa. En cas de que sigui correcte, demanar un altra vegada una altra
# opció i comprovar igualment que sigui correcte, com en el primer cas.
# En cas de que siguin les dues correctes indicar si ha guanyat el primer
# jugador, el segon o si hi ha empat.
print("Iniciando juego de piedra, papel, tijera ")
jugada = input("Jugador 1 introduce piedra, papel o tijera: ")
if jugada == "piedra" or jugada == "papel" or jugada == "tijera":
    print("Ok ")
    jugada2 = input("Jugador 2 introduce piedra, papel o tijera: ")
    if jugada2 == "piedra" or jugada2 == "papel" or jugada2 == "tijera":
        print("OK")
        if jugada == jugada2:
            print("Empate")
        elif jugada == "piedra" and jugada2 == "tijera":
            print("Gana el jugador 1")
        elif jugada == "papel" and jugada2 == "piedra":
            print("Gana el jugador 1")
        elif jugada == "tijera" and jugada2 == "papel":
            print("Gana el jugador 1")
        else:
            print("Gana el jugador 2")
    else:
        print("La jugada introducida no es correcta")
else:
    print("La jugada introducida no es correcta")
#   else:
#       print("Gana el jugador 2")
#if jugada == "piedra" or jugada == "papel" or jugada == "tijera":
 #   jugada2 = input("Ingresa la segunda jugada: ")
#elif jugada2 == "piedra" or jugada2 == "papel" or jugada2 == "tijera":
#    print("Gana el jugador")
#elif jugada + jugada2
#else:
#     print("La jugada introducida no es correcta")
