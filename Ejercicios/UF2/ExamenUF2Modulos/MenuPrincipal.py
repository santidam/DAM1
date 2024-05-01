"""Este Modulo contendrá el menú principal del programa, en él se ingresarán los comandos necesarios para 
     su ejecución y serán trasladados a la función correspondiente para su posterior ejecución en el modulo intérlprete"""

import interprete as mi



def main():
    """Esta función es el menu principal del programa Biblioteca, analiza los datos entrantes por el ususario y si cumple con el criterio
         de entrada las envia al interprete"""
    salir = False
    comandaLista = {"registrar": 4, "esborrar": 2, "list": 2, "setmana": 1,
                        "primera": 1}

    while salir == False:
        
        comando = input().lower()
        comandaFinal = comando.split(",")
        if comando == "exit":
            print("Cerrando programa...")
            salir = True
        elif len(comandaFinal) > 0 and comandaFinal[0] in comandaLista:
            if len(comandaFinal) == comandaLista[comandaFinal[0]]:
                mi.validarComando(comandaFinal)
            else:
                print("Error al introducir los elementos del comando")
        else:
            print("Error al introducir el comando")
       

main()

lista = ["registrar,aprobar,clase,02-02-2024"] 