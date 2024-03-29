# En este módulo principal añadiremos la función main que ejecutará el código del programa
# para ello, tendrá acceco a la librería interpret.
import ModulInterpret as mi


def main():
    """Esta función es el menu principal del programa Biblioteca, analiza los datos entrantes por el ususario y si cumple con el criterio
         de entrada las envia al interprete"""

    salir = False

    while salir == False:
        comandaLista = {"addllibre": 6, "startprestec": 4, "endprestec": 3, "listllibres": 1,
                        "listprestecs": 1, "listgenere": 2, "maxllibre": 1, "stats": 1, "info": 2}
        comanda = input("> ").lower()
        comandaFinal = comanda.split("-")
        if comanda == "quit":
            print("Cerrando programa...")
            salir = True
        elif len(comandaFinal) > 0 and comandaFinal[0] in comandaLista:
            if len(comandaFinal) == comandaLista[comandaFinal[0]]:
                mi.validarComando(comandaFinal)
            else:
                print("Error al introducir los elementos del comando")
        else:
            print("Error al introducir el comando")


pruebaAdd = "addLlibre-1234ab-Título1-Autor1-Acción-5"
pruebaStart = "startprestec-1234ab-Pepe-29/01/2024"
pruebaPrestamo = "endprestec-1234ab-30/01/2024"
pruebaPrestamo2 = "endprestec-1234ab-25/02/2024"

main()
# main(pruebaStart)
# main(pruebaPrestamo)
# main(pruebaPrestamo2)

