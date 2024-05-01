# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, procesando los datos y también
# se accederá a la base de datos del programa a traves del módulo base de datos.
import ficheros as fi
import hotel as h

def validarComando(comanda):
    """Esta funcion analiza  el comando introducido por el usuario y lo conecta con la función necesaria
        para su ejecución si cumple el criterio de entrada"""

    if comanda[0] == "afegir":
        if comanda[1] == "habitacio" :
            habitacion = comanda[2]
            capacidad = comanda[3]
            precio = comanda[4]
            if validar_datos(habitacion, "habitación") == True:
                if validar_datos(capacidad, "capacidad") == True:
                    if validar_datos(precio, "precio") == True:
                        h.afegir_habitacio(habitacion,capacidad,precio)
                        
                
        elif comanda[1] == "reserva" :
            habitacion = comanda[2]
            nombre = comanda[3]
            apellido = comanda[4]
            dni = comanda[5]
            telefono = comanda[6]

            if validar_datos(habitacion, "habitación") == True:
                if validarDNI(dni) == True and validarTelefono(telefono) == True:
                    h.afegir_reserva(habitacion, nombre, apellido, dni, telefono)


    elif comanda[0] == "finalitzar":
       habitacion = comanda[1]
       dias = comanda[2]
       if validar_datos(habitacion, "habitación") == True:
            if validar_negativo(dias) == True:
                print("Error: los días no pueden ser un número negativo")
            else:
                if validarNumeros(dias) == False:
                    print("Error: el numero de días introducido debe ser un número valido")
                else:
                    dias = int(dias)
                    if dias >= 0:
                        h.finalizar_reserva(habitacion, dias)
       

    elif comanda[0] == "netejar":
        habitacion = comanda[1]
        if validar_datos(habitacion, "habitación") == True:
            h.netejar_habitacion(habitacion)
        
    elif comanda[0] == "list":
        h.list()
    elif comanda[0] == "info":
            dni = comanda[1]
            if validarDNI(dni) == True:
                h.info_dni(dni)
    elif comanda[0] == "reserves":
        h.lista_reservas()


def validarNumeros(dato):
    """Esta función valdiará que un dato introducido sea un número retornando booleanos"""
    if dato.isdigit():
        return True
    else:
        return False


def validarMayor0(dato):
    """Esta función validará que un número sea mayor a 0, retorna booleanos"""

    if float(dato) > 0:
        return True
    else:
        return False


def validarDNI(dato):
    """Esta función validará que un dni tenga 6 caracteres alfanumericos, retorna booleanos"""
    if len(dato) == 9:
        return True
    else:
        print("Error: el DNI introducido no es válido")
        return False


4
def validarTelefono(dato):
    """Esta función validará que el telefono introducido sea valido, 6 caracteres y solo números, tras lo cual retorna True o False"""
    if validarNumeros(dato) == True and len(dato) == 9:
        return True
    else:
        print("Error: el telefono introducido no es valido")
        return False



def validarFloatNumero(numero):
    """Esta función analiza un número y determina si es un float retornando True o False"""
    if numero.count(".") == 1:
        numero = numero.split(".")
        if validarNumeros(numero[0]) == True and validarNumeros(numero[1]) == True:
            return True
        else:
            return False
    else:
        return False
    
def validar_negativo(dato):
    """Función para validar si el valor ingresado es negativo retorna True si es negativo y False en caso contrario """
    if dato.count("-") == 1 and dato[0] == "-":
        dato = dato.split("-")
        if dato[1].isdigit() == True:
            return True
        else:
            return False
    else:
        return False
    

def validar_datos(dato, tipo ):
    """Esta función determina si los datos introducidos cumplen el criterio de entrada: dato positivo, numero valido, mayor a 0 y
        retorna True si los cumple y si no los cumple informa el error"""
    
    if validar_negativo(dato) == True:
        print(f"Error de {tipo}: el número introducido no puede ser negativo")
    else:
        if validarNumeros(dato) == False:
                    print(f"Error de {tipo}: el dato introducido debe ser un número valido")
        else:
            if validarMayor0(dato) == False:
                        print(f"Error de {tipo}: el número introducido debe ser mayor a 0")
            else:
                return True