#    El sistema genera aleatòriament un número de l'1 al 50.
# L'usuari té un total de 5 possibilitats d'endevinar el número.
# Si el número endevinat per l'usuari és més gran que el número donat pel
# sistema, imprimiu "massa gran".
# Si el número endevinat per l'usuari és menor que el número proporcionat
# pel sistema, imprimiu "massa petit".
# Si el número endevinat per l'usuari és igual al número donat pel sistema,
# imprimiu "Felicitacions" i sortiu del bucle.
# Si gastem les cinc oportunitats i no encertem el número, imprimirem: "Has
# perdut" i el programa finalitzarà mostrant el número generat.

import random

numero = random.randint(1, 50)
print("Iniciando adivina el número: ")
user = int(input("Introduce un número: "))
if user <= 0:
    print("Numero introducido invalido")
else:
    intento = 1
    while intento <= 4 :
        if user == numero:
            print("Has ganado !")
           # break
    #    elif intento == 5:
     #       print("Has perdido !")
            #break
        while user > numero and intento <= 4:
            print("Número introducido demasiado grande")
            user = int(input("Introduce otro número: "))
            intento += 1
        while user < numero and intento <= 4:
            print("Numero intoducido demasiado pequeño")
            user = int(input("Introduce otro número: "))
            intento += 1
    else:
        print("Has perdido")

        # Fallo => te permite 6 intentos