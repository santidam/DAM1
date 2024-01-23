import datetime
import ModulBiblioteca as mb


def validarLenComando(comanda):
    """Esta funcion analiza la logitud del comando introducido por el usuario, validando su solicitud"""

    diccLensComandos = {"addllibre": 6, "startprestec": 4, "endprestec": 3, "listllibres": 1,
                        "listprestecs": 1, "listgenere": 2, "masllibre": 1, "stats": 1, "info": 2}
    listaComanda = comanda.split("-")
    print(listaComanda)
    if listaComanda[0] in diccLensComandos:
        if len(listaComanda) == diccLensComandos[listaComanda[0]]:

            return print("OK")
        else:
            print("Error en la longitud del comando")
    else:
        print("error de comando")
