# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, también
# se accederá a la base de datos del programa a traves del módulo bliblioteca.
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
            if listaComanda[0] == "addllibre":
                print(mb.diccLibrosStart(listaComanda))
            elif listaComanda[0] == "startprestec":

                return print("OK")
        else:
            print("Error en la longitud del comando")
    else:
        print("error de comando")

def entradaFecha(fecha):
    """Esta función analiza la entrada de fechas en formato d/m/a y retorna 
        una lista con fechas en a/m/d y a/m/d + 15 dias"""
    fechaEntrada = datetime.strptime(fecha, "%d/%m/%a")
    fechaSalida =  datetime.strptime(fechaEntrada, "%a/%m/%d")
    fechaModificada = fechaSalida + datetime.timedelta(days=15)
    fechaSalidaModificada = datetime.strptime(fechaModificada, "%a/%m/%d")
    return [fechaSalida, fechaSalidaModificada]


