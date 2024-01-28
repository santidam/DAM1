# En este módulo principal añadiremos la función main que ejecutará el código del programa
# para ello, tendrá acceco a la librería interpret.
import ModulInterpret as mi


def main(comanda):

    salir = False

    while salir == False:
        comandaLista = ["addllibre", "startprestec", "endprestec", "listllibres",
                        "listprestecs", "listgenere", "masllibre", "stats", "info"]
        comanda = input("> ").lower()
        comandaFinal = comanda.split("-")
        if comanda == "quit":

            salir = True
        elif len(comandaFinal) >= 1 and comandaFinal[0] in comandaLista:
            mi.validarLenComando(comanda)


comanda = "addLlibre-1234ab-Título1-Autor1-Acción-5"
main(comanda)
