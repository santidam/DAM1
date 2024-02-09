# En este módulo interprete se ejecturan las funciones que se llevaran a cabo en el módulo principal, procesando los datos y también
# se accederá a la base de datos del programa a traves del módulo base de datos.
import ficheros as fi

def validarComando(comanda):
    """Esta funcion analiza  el comando introducido por el usuario y lo conecta con la función necesaria
        para su ejecución si cumple el criterio de entrada"""

    if comanda[0] == "afegir":
        if comanda[1] == "habitacio" :
            habitacion = comanda[2]
            capacidad = comanda[3]
            precio = comanda[4]
            if validarNumeros(habitacion) == True and validarNumeros(capacidad) == True and validarNumeros(precio) == True:
                if validarMayor0(habitacion) == True and validarMayor0(capacidad) == True and validarMayor0(precio) == True:
                    fi.afegir_habitacio(habitacion,capacidad,precio)
            #     else:
            #         print("Error: Todos los valores introducidos en la comanda [habitación] [capacidad] [precio] deben ser mayores a 0")
            # else:
            #     print("Error: Todos los valores introducidos en la comanda [habitación] [capacidad] [precio] deben ser números")
                
        elif comanda[1] == "reserva" :
            habitacion = comanda[2]
            nombre = comanda[3]
            apellido = comanda[4]
            dni = comanda[5]
            telefono = comanda[6]
            if validarDNI(dni) == True and validarTelefono(telefono) == True:
                fi.afegir_reserva(habitacion, nombre, apellido, dni, telefono)


    elif comanda[0] == "finalitzar":
       habitacion = comanda[1]
       dias = comanda[2]
       if validarNumeros(dias) == True:
           dias = int(comanda[2])
           fi.finalizar_reserva(habitacion, dias)
       

    elif comanda[0] == "netejar":
        habitacion = comanda[1]
        fi.netejar_habitacion(habitacion)
        
    elif comanda[0] == "list":
        fi.list()
    elif comanda[0] == "info":
            dni = comanda[1]
            if validarDNI(dni) == True:
                fi.info_dni(dni)
    elif comanda[0] == "reserves":
        fi.lista_reservas()

def validarNumeros(dato):
    """Esta función valdiará que un dato introducido sea un número"""
    if dato.isdigit():
        return True
    else:
        print(f"Error: el dato introducido {dato} debe ser un número")
        return False
def validarMayor0(dato):
    """Esta función validará que un número sea mayor a 0"""
    if int(dato) > 0:
        return True
    else:
        print(f"Error: el número introducido {dato} debe ser mayor a 0")
        return False

def validarDNI(dato):
    """Esta función validará que un dni tenga 6 caracteres alfanumericos"""
    if len(dato) == 9:
        return True
    else:
        print("Error: el DNI introducido no es válido")
        return False
def validarTelefono(dato):
    """Esta función validará que el telefono introducido sea valido, 6 caracteres y solo números"""
    if validarNumeros(dato) == True and len(dato) == 9:
        return True
    else:
        print("Error: el telefono introducido no es valido")
        return False
