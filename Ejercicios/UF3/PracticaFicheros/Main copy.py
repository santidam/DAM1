"""Este Modulo contendrá el menú principal del programa, en él se ingresarán los comandos necesarios para 
     su ejecución y serán trasladados a la función correspondiente para su posterior ejecución en el modulo intérlprete"""

import Interprete as mi
import sys

com = [
    'Afegir habitacio -1 4 50',
    'afegir habitacio 0 1 50',
    'afegir habitacio 1 0 40',
    'afegir habitacio aa 1 40',
    'afegir habitacio 100 aa 50',
    'afegir habitacio 100 1 -1',
    'afegir',
    'afegir habitacio',
    'afegir reserva',
    'afegir reserva -1 hornos jordi 123 123',
    'afegir reserva 0 hornos jordi 123 123',
    'afegir reserva 100 hornos jordi 123456789 123123123',
    'afegir reserva 100 hornos jordi 12345678z 123',
    'finalitzar',
    'finalitzar 100 -1',
    'netejar',
    'netejar 100',
    'finalitzar 100 5',
    'list',
    'info 12345678Z',
    'info asdf asdf',
    'reserves',
    'reserves 234',
    'afegir habitacio 104 4 50',
    'reserves',
    'list',
    'afegir reserva 104 hornos jordi 12345678z 123456789',
    'afegir habitacio 105 2 60',
    'list',
    'finalitzar 100 0',
    'finalitzar 105 4',
    'afegir habitacio 106 2 40',
    'afegir reserva 105 segura albert 45790286t 123456789',
    'info 12345678z',
    'info 23415678E',
    'reserves',
    'finalitzar 104 0',
    'list',
    'finalitzar 105 4',
    'list',
    'netejar 106',
    'netejar 104',
    'netejar 105',
    'list',
]




def main():
    """Esta función es el menu principal del programa hotel¡, analiza los datos entrantes por el ususario y si cumple con el criterio
         de entrada las envia al interprete"""
    comandaLista = {"afegir habitacio": 5, "afegir reserva": 7, "finalitzar": 3, "netejar": 2,
                        "list": 1, "info": 2, "reserves": 1}
    
    for comand in com:

        comandaFinal = comand.split(" ")
        
        print(comandaFinal)

   
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
            print("Error al introducir el comando\nIntroduzca un comando valido\nLista de comandos: ")
            for i, valor in comandaLista.items():
                print(i,"==> Argumentos:", valor)

       
# args = sys.argv
# del args[0]
main()