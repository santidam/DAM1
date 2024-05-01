"""Este modulo 'hotel' se ocupará de la parte lógica de los procesos del programa, realizando las gestiones de datos y mostrando la información obtenida
    del módulo ficheros"""
import ficheros as fi



diccHabitaciones = fi.getdicc("habitaciones")
diccReservas = fi.getdicc("reservas")

def afegir_habitacio(habitacion, capacidat, precio):
    """Este comando registrará las habitaciones en la base de datos"""
    if habitacion in diccHabitaciones:
        print(f"Error: ya existe una habitación registrada con el número {habitacion}")
    else:
        diccHabitaciones[habitacion] = {"capacidad": capacidat, "precio": precio, "estado": "disponible"}
        fi.append_ficheros_habitacion(habitacion, capacidat, precio, "disponible")


def afegir_reserva(habitacion, nombre, apellido, dni, telefono):
    """Este comando registrará las reservas en la base de datos del programa"""
    if habitacion in diccReservas:
        print("Error: la habitación seleccionada no se encuentra disponible")
    else:
        if habitacion not in diccHabitaciones:
            print("Error: no existe ninguna habitación con el número ingresado")
        else:
            if diccHabitaciones[habitacion]["estado"] != "disponible":
                print("La habitación seleccionada no está disponible (bruta)")
            else:
                diccReservas[habitacion] = {"nombre":nombre, "apellido": apellido, "dni": dni, "telefono": telefono}
                fi.append_ficheros_reservas(habitacion, nombre, apellido, dni, telefono)
                modificar_disponibilidad(habitacion, "no disponible")



def modificar_disponibilidad(habitacion, estado):
    """Esta función modificara la disponibilidad de las habitaciones en diccHabitaciones """
    diccHabitaciones[habitacion]["estado"] = estado
    fi.modificar_archivo_habitaciones()


def finalizar_reserva(habitacion, dias):
    """Esta función finalizará la reserva de una habitación"""
    if habitacion not in diccHabitaciones:
        print("Error: no existe ninguna habitación con el número ingresado")
    else:
        if habitacion not in diccReservas:
            print("Error: no existe ninguna reserva con el número ingresado")
        else:
            del diccReservas[habitacion]
            fi.modificar_archivo_reservas()
            if dias == 0:
                print("Reserva anulada. Sin coste para el cliente. La habitación vuelve a estar disponible")
                modificar_disponibilidad(habitacion,"disponible")
                fi.modificar_archivo_habitaciones()
            else:
                calcular_cuota(habitacion, dias)
                modificar_disponibilidad(habitacion, "bruta")
                print("L'habitacio queda en espera del servei de nateja")
            
                fi.modificar_archivo_habitaciones()


def calcular_cuota(habitacion,dias):
    """Esta función recibe el numero de habitacion y los días transcurridos de reserva, y calcula el monto total de la reserva"""
    total = float(diccHabitaciones[habitacion]['precio']) * dias
    print(f"Preu total de la estada: {total} €")

def netejar_habitacion(habitacion):
    """Esta función limpiará las habitaciones que se encuentren en estado 'bruta'"""
    if habitacion not in diccHabitaciones:
        print("Error: la habitación seleccionada no existe")
    else:
        if diccHabitaciones[habitacion]["estado"] != "bruta":
            print("La habitación seleccionada no está sucia")
        else:
            modificar_disponibilidad(habitacion, "disponible")
            fi.modificar_archivo_habitaciones()
            print("El servicio de habitaciones ha realizado la limpieza correctamente.\nLa habitación ha quedado disponible ")


def list():
    """Esta función listará la información de todas las habitaciones del hotel"""
    if not diccHabitaciones:
        print("No existen habitaciones registradas")
    else:
        print(f"========   INFO HOTEL     {'='* 100}\n"
              "Hab      Cap     Estat")
        disponible = 0
        ocupada = 0
        bruta = 0
        for clave, valor in diccHabitaciones.items():
            if diccHabitaciones[clave]['estado'] == "no disponible":
                ocupada += 1
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado'].upper()}     => Cient: {diccReservas[clave]['nombre'].capitalize()} {diccReservas[clave]['apellido'].capitalize()}")
            elif diccHabitaciones[clave]['estado'] == "disponible":
                disponible += 1
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado'].upper()}")
            else:
                bruta += 1
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado'].upper()}")
            print("-" * 126)
        print("=" * 126)
        print(f"Total habitaciones: {len(diccHabitaciones)}")
        print(f"Disponibles: {disponible}    Ocupadas: {ocupada}  Sucias: {bruta}")            


def info_dni(dni):
    """Esta función mostrará los datos de los clientes con reserva por DNI"""
    if not diccReservas:
        print("Error: actualmente no hay clientes hospedados")
    else:
        listaClaves = []
        for clave, dato in diccReservas.items():
            for x , y in dato.items():
                if y == dni:
                    listaClaves.append(clave)
                   
        if len(listaClaves) == 0:
            print("No existe ningún huesped con el DNI introducido")
        else:
            nombre = diccReservas[listaClaves[0]]["nombre"]
            apellido = diccReservas[listaClaves[0]]["apellido"]
            print(f"Datos del cliente:              {diccReservas[listaClaves[0]]['apellido'].capitalize()} , {diccReservas[listaClaves[0]]['nombre'].capitalize()}  -  Telefono: {diccReservas[listaClaves[0]]['telefono']}")

            for i in range(len(listaClaves)):
                print(f"Habitación: {listaClaves[i]}")




def lista_reservas():
    """Esta función muestra toda la información de las reservas del hotel..."""
    if not diccReservas:
        print("Actualmente no hay reservas registradas")
    else:
        print("========         RESERVAS        ========")
        for i in diccReservas:
            print(f"{i}  :   {diccReservas[i]['dni'].upper()}  -  {diccReservas[i]['nombre'].capitalize()}  {diccReservas[i]['apellido'].capitalize()}  -  {diccReservas[i]['telefono']}")
            print("-"*150)
