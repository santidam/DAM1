# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, procesando los datos y también
# se accederá a la base de datos del programa a traves del módulo base de datos.
import BaseDatos as bd

def validarComando(comanda):
    """Esta funcion analiza  el comando introducido por el usuario y lo conecta con la función necesaria
        para su ejecución si cumple el criterio de entrada"""

    if comanda[0] == "registrar":
       mision = comanda[1]
       lugar = comanda[2]
       fecha = comanda[3]
       bd.registrar(mision,lugar,fecha)

    elif comanda[0] == "esborrar":
        mision = comanda[1]
        bd.esborrarMision(mision)
        
    elif comanda[0] == "list":
        año = comanda[1]
        bd.listAnyo(año)
        
    elif comanda[0] == "setmana":
        bd.setmana()
    elif comanda[0] == "primera":
        bd.primera()