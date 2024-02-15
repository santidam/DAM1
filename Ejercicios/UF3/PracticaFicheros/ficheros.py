"""Este modulo gestionara los procesos de los ficheros
    realizando las funciones de guardado y analisis de datos del programa"""
import os

nombre_carpeta = "./ficheros"
ruta_archivo = nombre_carpeta +"/habitacions.txt"
ruta_archivo2 = nombre_carpeta +"/reserves.txt"

diccHabitaciones = {}
diccReservas = {}



def modificar_archivo_habitaciones():
    """Esta función actualiza el archivo de habitaciones con los datos de diccHabitaciones."""
    f = open(ruta_archivo, "w")
    for habitacion, datos in diccHabitaciones.items():
        f.write(f"{habitacion},{datos['capacidad']},{datos['precio']},{datos['estado']}\n")
    f.close()

def modificar_archivo_reservas():
    """Esta función actualizará el estado del fichero reservas"""
    f = open(ruta_archivo2, "w")
    for habitacion, datos in diccReservas.items():
        f.write(f"{habitacion},{datos['nombre']},{datos['apellido']},{datos['dni']},{datos['telefono']}\n")
    f.close()






def crear_carpeta():
    """Esta función comprueba la existencia de la carpeta contenedora de los ficheros, en caso de no existir,
        crea la carpeta. Si la carpeta existe, comprueba la existencia de los ficheros y lee el contenido 
        pasando así la información a los diccionarios correspondientes (diccHabitaciones, diccReservas)"""

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
                capacidad = linea[1]
                precio = float(linea[2])
                estado = linea[3].replace("\n", "")
                diccHabitaciones[habitacion] = {"capacidad": capacidad, "precio": precio, "estado": estado}
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
        print("La carpeta ficheros no existe...\nCreando carpeta")
        os.mkdir(nombre_carpeta)

def append_ficheros_habitacion(habitacion, capacidat, precio, estado):
    """Esta funcion agrega a la línea final de los ficheros una nueva línea de datos al fichero habitaciones.txt"""
    
    f = open(ruta_archivo, "a")
    f.write(habitacion + "," + capacidat + "," + precio + "," + estado + "\n")
    f.close()
    print("Habitación registrada")

def append_ficheros_reservas(habitacion, nombre, apellido, dni, telefono):
    """Esta función guarda los datos de las reserva en un fichero de texto"""
    
    f = open(ruta_archivo2, "a")
    f.write(habitacion + "," + nombre + "," + apellido + "," + dni + "," + telefono + "\n")
    f.close()
    print("Reserva registrada")


def getdicc(tipo):
    """Esta función recibe el tipo de diccionario a enviar, y retorna la información de los diccionarios obtenidos de los ficheros"""
    if tipo == "habitaciones":
        return diccHabitaciones
    elif tipo == "reservas":
        return diccReservas

crear_carpeta()