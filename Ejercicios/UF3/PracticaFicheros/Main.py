"""Este Modulo contendrá el menú principal del programa, en él se ingresarán los comandos necesarios para 
     su ejecución y serán trasladados a la función correspondiente para su posterior ejecución en el modulo intérlprete"""

import Interprete as mi
import sys


def main(comandaFinal):
    """Esta función es el menu principal del programa hotel¡, analiza los datos entrantes por el ususario y si cumple con el criterio
         de entrada las envia al interprete"""
    comandaLista = {"afegir habitacio": 5, "afegir reserva": 7, "finalitzar": 3, "netejar": 2,
                        "list": 1, "info": 2, "reserves": 1}

   
    if comandaFinal[0] == "afegir":
        if comandaFinal[1] == "habitacio" and len(comandaFinal) == comandaLista["afegir habitacio"]:
             mi.validarComando(comandaFinal)
                
        elif comandaFinal[1] == "reserva" and len(comandaFinal) == comandaLista["afegir reserva"]:
            mi.validarComando(comandaFinal)

        else:
            print("Error: Número de argumentos incorrecto")
                
    elif len(comandaFinal) > 0 and comandaFinal[0] in comandaLista:
    
        if len(comandaFinal) == comandaLista[comandaFinal[0]]:
            mi.validarComando(comandaFinal)
        else:
            print("Error: Numero de argumentos incorrecto")
    else:
        print("Error al introducir el comando")
       
args = sys.argv
del args[0]
main(args)