"""Este modulo gestionara los procesos de la base de datos del programa en ficheros
    realizando las funciones de guardado y analisis de datos del programa"""
import os



diccHabitaciones = {}
diccReservas = {}

def afegir_habitacio(habitacion, capacidat, precio):
    """Este comando registrará las habitaciones en la base de datos"""
    if habitacion in diccHabitaciones:
        print(f"Error: ya existe una habitación con el número {habitacion}")
    else:
        diccHabitaciones[habitacion] = {"capacidad": capacidat, "precio": precio, "estado": "disponible"}
        append_ficheros_habitacion(habitacion, capacidat, precio, "disponible", "/habitacions.txt" )



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
                append_ficheros_reservas(habitacion, nombre, apellido, dni, telefono, "/reserves.txt")
                modificar_disponibilidad(habitacion, "no disponible")




def modificar_disponibilidad(habitacion, estado):
    """Esta función modificara la disponibilidad de las habitaciones en diccHabitaciones """
    diccHabitaciones[habitacion]["estado"] = estado
    modificar_archivo_habitaciones()


def modificar_archivo_habitaciones():
    """Esta función actualiza el archivo de habitaciones con los datos de diccHabitaciones."""
    ruta_archivo = "./ficheros/habitacions.txt"
    f = open(ruta_archivo, "w")
    for habitacion, datos in diccHabitaciones.items():
        f.write(f"{habitacion},{datos['capacidad']},{datos['precio']},{datos['estado']}\n")

def modificar_archivo_reservas():
    """Esta función actualizará el estado del fichero reservas"""
    ruta_archivo = "./ficheros/reserves.txt"
    f = open(ruta_archivo, "w")
    for habitacion, datos in diccReservas.items():
        f.write(f"{habitacion},{datos['nombre']},{datos['apellido']},{datos['dni']},{datos['telefono']}\n")



def finalizar_reserva(habitacion, dias):
    """Esta función finalizará la reserva de una habitación"""
    if habitacion not in diccHabitaciones:
        print("Error: no existe ninguna habitación con el número ingresado")
    else:
        if habitacion not in diccReservas:
            print("Error: no existe ninguna reserva con el número ingresado")
        else:
            del diccReservas[habitacion]
            modificar_archivo_reservas()
            if dias == 0:
                print("Reserva anulada. Sin coste para el cliente. La habitación vuelve a estar disponible")
                modificar_disponibilidad(habitacion,"disponible")
                modificar_archivo_habitaciones()
            else:
                calcular_cuota(habitacion, dias)
                modificar_disponibilidad(habitacion, "bruta")
                print("L'habitacio queda en espera del servei de nateja")
            
                modificar_archivo_habitaciones()

def calcular_cuota(habitacion,dias):
    """Esta función calcula el monto total de la reserva"""
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
            modificar_archivo_habitaciones()
            print("El servicio de habitaciones ha hecho su fuckin trabajo. La habitación ha quedado disponible ")



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
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado']}     => Cient: {diccReservas[clave]['nombre']} {diccReservas[clave]['apellido']}")
            elif diccHabitaciones[clave]['estado'] == "disponible":
                disponible += 1
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado']}")
            else:
                bruta += 1
                print(f"{clave}       {diccHabitaciones[clave]['capacidad']}    {diccHabitaciones[clave]['estado']}")
        print("=" * 126)
        print(f"Total habitaciones: {len(diccHabitaciones)}")
        print(f"Disponibles: {disponible}    Ocupadas: {ocupada}  Sucias: {bruta}")



def info_dni(dni):
    """Esta función mostrará los datos de los clientes con reserva por DNI"""
    if not diccReservas:
        print("Error: actualmente no hay clientes hospedados")
    else:
        diccDNI = {}
        listaClaves = []
        for clave, dato in diccReservas.items():
            for x , y in dato.items():
                if y == dni:
                    nombre = diccReservas[clave]["nombre"] + " " + diccReservas[clave]["apellido"]
                    if nombre not in diccDNI[str(diccReservas[clave]["nombre"] + " " + diccReservas[clave]["apellido"])]:
                        diccDNI[[clave]["nombre"] +" "+ diccReservas[clave]["apellido"]] = [clave]
                    else:
                        diccDNI[[clave]["nombre"] +" "+ diccReservas[clave]["apellido"]].append(clave)
                    listaClaves.append(clave)
        print(diccDNI)            
        if len(listaClaves) == 0:
            print("No existe ningún huesped con el DNI introducido")
        else:
            nombre = diccReservas[listaClaves[0]]["nombre"]
            apellido = diccReservas[listaClaves[0]]["apellido"]
            diccDNI = {}
            for i in range(len(listaClaves)):
                print(f"Datos del cliente:              {diccReservas[listaClaves[i]]['apellido']} , {diccReservas[listaClaves[i]]['nombre']}  -  Telefono: {diccReservas[listaClaves[i]]['telefono']}")

            for i in range(len(listaClaves)):
                print(f"Habitación: {listaClaves[i]}")

def lista_reservas():
    """Esta función muestra toda la información de las reservas del hotel..."""
    if not diccReservas:
        print("Actualmente no hay reservas registradas")
    else:
        print("========         RESERVAS        ========")
        for i in diccReservas:
            print(f"{i}  :   {diccReservas[i]['dni']}  -  {diccReservas[i]['nombre']}  {diccReservas[i]['apellido']}  -  {diccReservas[i]['telefono']}")

        # dicInfo = {}
        # for clave, dato in diccReservas.items():
        #     if diccReservas[clave]["nombre"] not in dicInfo:
        #         dicInfo[diccReservas[clave]["nombre"]] = {"habitacion":[clave]}
        #     else:
        #         dicInfo[diccReservas[clave]["nombre"]]["habitacion"].append(clave)






def crear_carpeta():
    nombre_carpeta = "./ficheros"
    ruta_archivo = nombre_carpeta +"/habitacions.txt"
    ruta_archivo2 = nombre_carpeta +"/reserves.txt"

    # si existe la carpeta
    if os.path.exists(nombre_carpeta):
        # miramos si existe el fichero de datos
        if os.path.exists(ruta_archivo):
            # abrimos para leemos los datos
            f = open(ruta_archivo, "r")
            lineas = f.readlines()
            f.close()
            for linea in lineas:
                linea = linea.split(",")
                habitacion = linea[0]
                capacidat = linea[1]
                precio = float(linea[2])
                estado = linea[3].replace("\n", "")
                diccHabitaciones[habitacion] = {"capacidad": capacidat, "precio": precio, "estado": estado}
        if os.path.exists(ruta_archivo2):
            # abrimos para leemos los datos
            f = open(ruta_archivo2, "r")
            lineas = f.readlines()
            f.close()
            for linea in lineas:
                linea = linea.split(",")
                habitacion = linea[0]
                nombre = linea[1]
                apellido = linea[2]
                dni = linea[3]
                telefono = linea[4].replace("\n", "")
                diccReservas[habitacion] = {"nombre": nombre, "apellido": apellido, "dni": dni, "telefono": telefono}

    else:
        print("La carpeta no existe...\n Creando carpeta")
        os.mkdir(nombre_carpeta)

def append_ficheros_habitacion(habitacion, capacidat, precio, estado, ruta_archivo):
    """Esta funcion """
    ruta_archivo2 = "./ficheros" + ruta_archivo
    
    f = open(ruta_archivo2, "a")
    f.write(habitacion + "," + capacidat + "," + precio + "," + estado + "\n")
    f.close()
    print("Habitación registrada")

def append_ficheros_reservas(habitacion, nombre, apellido, dni, telefono, ruta_archivo):
    """Esta función guarda los datos de las reserva en un fichero de texto"""
    ruta_archivo2 = "./ficheros" + ruta_archivo
    
    f = open(ruta_archivo2, "a")
    f.write(habitacion + "," + nombre + "," + apellido + "," + dni + "," + telefono + "\n")
    f.close()
    print("Reserva registrada")



crear_carpeta()