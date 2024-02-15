"""Este Modulo contendrá el menú principal del programa, en él se ingresarán los comandos necesarios para 
     su ejecución y serán trasladados a la función correspondiente para su posterior ejecución en el modulo intérlprete"""

import Interprete as mi
import sys


def main(comandaFinal):
    """Esta función es el menu principal del programa hotel¡, analiza los datos entrantes por el ususario y si cumple con el criterio
         de entrada las envia al interprete"""
    comandaLista = {"afegir habitacio": 5, "afegir reserva": 7, "finalitzar": 3, "netejar": 2,
                        "list": 1, "info": 2, "reserves": 1}

   
    if comandaFinal[0] == "afegir" and len(comandaFinal) > 1:
        if comandaFinal[1] == "habitacio" and len(comandaFinal) == comandaLista["afegir habitacio"]:
             mi.validarComando(comandaFinal)
                
        elif comandaFinal[1] == "reserva" and len(comandaFinal) == comandaLista["afegir reserva"]:
            mi.validarComando(comandaFinal)

        else:
            print(f"Error en el comando {comandaFinal[0] + ' ' + comandaFinal[1]}: Número de argumentos incorrecto. Debe contener: {comandaLista[comandaFinal[0]+' '+comandaFinal[1]]} argumentos")
                
    elif len(comandaFinal) > 0 and comandaFinal[0] in comandaLista:
    
        if len(comandaFinal) == comandaLista[comandaFinal[0]]:
            mi.validarComando(comandaFinal)
        else:
            print(f"Error en el comando {comandaFinal[0]}: Numero de argumentos incorrecto. Debe contener {comandaLista[comandaFinal[0]]} argumentos")
    else:
        print("Error al introducir el comando\nIntroduzca un comando valido:")
        for i, valor in comandaLista.items():
            print(i,"==> Argumentos:", valor)

       
args = sys.argv[1:]
argumentos = []

for i in args:
    argumentos.append(i.lower())
    
main(argumentos)