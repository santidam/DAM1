# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, también
# se accederá a la base de datos del programa a traves del módulo bliblioteca.
from datetime import datetime, timedelta
import ModulBiblioteca as mb


def validarLenComando(comanda):
    """Esta funcion analiza la logitud del comando introducido por el usuario, validando su solicitud"""

    # diccLensComandos = {"addllibre": 6, "startprestec": 4, "endprestec": 3, "listllibres": 1,
    #                     "listprestecs": 1, "listgenere": 2, "masllibre": 1, "stats": 1, "info": 2}
    # listaComanda = comanda.split("-")
    # # print(listaComanda)
    # if listaComanda[0] in diccLensComandos:
    # if len(listaComanda) == diccLensComandos[listaComanda[0]]:
    if comanda[0] == "addllibre":
        if int(comanda[5]) > 0:
            print(mb.diccLibrosStart(comanda))
        else:
            print("Error, número de páginas debe ser mayor a 0")
    elif comanda[0] == "startprestec":
        if mb.disponibilidad(comanda[1]) == False:
            return f"El libro con el código {comanda[1]} no se encuentra disponible"
        else:
            fechaInicio, fechaFinal = entradaFecha(comanda[3])
            return mb.startPrestec(comanda, fechaInicio, fechaFinal)

        # return print("OK")
    # else:
    #     print("Error en la longitud del comando")


def entradaFecha(fecha):
    """Esta función analiza la entrada de fechas en formato d/m/a y retorna 
        una lista con 2 fechas: en a/m/d y a/m/d + 15 dias"""
    fechaEntrada = datetime.strptime(fecha, "%d/%m/%Y")
    fechaModificada = fechaEntrada + timedelta(days=15)

    fechaSalida = fechaEntrada.strftime("%Y/%m/%d")
    fechaSalidaModificada = fechaModificada.strftime("%Y/%m/%d")
    return fechaSalida, fechaSalidaModificada
