import ModulInterpret as mi


def main():

    salir = False

    while salir == False:

        comanda = input("> ").lower()
        if comanda == "quit":
            salir = True
        elif len(comanda.split("-")) >= 1:
            mi.validarLenComando(comanda)


main()
