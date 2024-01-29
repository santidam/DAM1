# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, procesando losdatos y también
# se accederá a la base de datos del programa a traves del módulo bliblioteca.
from datetime import datetime, timedelta
import ModulBiblioteca as mb


def validarLenComando(comanda):
    """Esta funcion analiza  el comando introducido por el usuario y lo conecta con la función necesaria
        para su ejecución si cumple el criterio de entrada"""

    if comanda[0] == "addllibre":
        if comanda[5].isdigit() and int(comanda[5]) > 0:
            print(mb.diccLibrosStart(comanda))
        else:
            print("Error, número de páginas debe ser mayor a 0")
    elif comanda[0] == "startprestec":
        disponibilidad =  mb.disponibilidad(comanda[1])
        if disponibilidad == False:
           print(f"El libro con el código {comanda[1]} no se encuentra disponible")
        elif disponibilidad == True:
            fechaInicio, fechaFinal = entradaFecha(comanda[3])
            print(mb.startPrestec(comanda, fechaInicio, fechaFinal))
    elif comanda[0] == "endprestec":
        disponibilidad =  mb.disponibilidad(comanda[1])
        if disponibilidad == True:
                print(f"El libro con el código {comanda[1]} no se encuentra en prestamo actualmente")
        elif  disponibilidad == False:
            x, y = entradaFecha(comanda[2])
            fechaRetorno = mb.fechaRetorno(comanda[1], x)
            if fechaRetorno == True:
                mb.endPrestec(comanda[1])
            elif fechaRetorno == False:
                mb.Incidencia(comanda[1], x)
    #elif comanda[0] == "listllibres":

def entradaFecha(fecha):
    """Esta función analiza la entrada de fechas en formato d/m/a y retorna 
        una lista con 2 fechas: en a/m/d y a/m/d + 15 dias"""
    fechaEntrada = datetime.strptime(fecha, "%d/%m/%Y")
    fechaModificada = fechaEntrada + timedelta(days=15)

    fechaSalida = fechaEntrada.strftime("%Y/%m/%d")
    fechaSalidaModificada = fechaModificada.strftime("%Y/%m/%d")
    return fechaSalida, fechaSalidaModificada

