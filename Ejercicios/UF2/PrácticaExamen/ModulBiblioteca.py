# En este módulo se almacenarán las bases de datos del programa, siendo accesibles
# desde el módulo interpret
# import ModulInterpret as mi
from datetime import datetime

diccLibros = {}  # diccionario de libros
diccPrestamos = {}  # diccionarios de alumnos con prestamos
diccIncidiencias = {}


def diccLibrosStart(listaComanda):
    """Esta función contendrá la base de datos de los libros: registro y disponibilidad"""
    if listaComanda[1] in diccLibros:
        return f"Error, el codigo del libro {listaComanda[1]} ya ha sido registrado"
    else:
        diccLibros[listaComanda[1]] = {"titulo": listaComanda[2], "autor": listaComanda[3],
                                       "genero": listaComanda[4], "paginas": listaComanda[5], "disponibilitat": True, "fechaEntrega": None}
        return f"Libro con coódigo {listaComanda[1]} registrado correctamente"


def startPrestec(listaComanda, fechaInicio, fechaFinal):
    """Esta función módificara la disponibilidad de los libros añadiendo la fecha de inicio del prestamo y de la finalización que
        será 15 días despues"""


    diccPrestamos[listaComanda[1]] = {
        "Alumno": listaComanda[2], "fecha prestamo": fechaInicio, "fecha entrega": fechaFinal}
    diccLibros[listaComanda[1]]["disponibilitat"] = False

    return f"Prestamo realizado. El libro se debe entregar el {fechaFinal}"

def endPrestec(codigo):
    """Esta función finaliza un préstamo que haya sido entregado en un tiempo dentro del rango del prestamo, cambiando la disponiblidad del libro y quitando el libro
        del diccionario de Prestamos"""
    diccLibros[codigo]["disponibilitat"] =  True
    diccPrestamos[codigo] = {}
    print("Devolución procesada correctamente")

def Incidencia(codigo, fechaEntrega ):
    """Esta función registra las incidencias de los usuarios accediendo a los datos del
        diccionario de Prestamos con el codigo de entrada de la función"""

    nombre = diccPrestamos[codigo]["Alumno"]
    fechaPrestamo = diccPrestamos[codigo]["fecha prestamo"]
    fechaDevolucion = diccPrestamos[codigo]["fecha entrega"]
    if nombre not in diccIncidiencias:
        print("El usario no tiene incidencias previas... Generando nueva incidencia")
        diccIncidiencias[nombre] = [{"codigo": codigo, "fecha prestamo": fechaPrestamo, "fecha devolucion": fechaDevolucion, "fecha entrega": fechaEntrega}]
        endPrestec(codigo)
        print(diccIncidiencias)
    else:
        print("El usario tiene incidencias previas... Generando nueva incidencia")
        diccIncidiencias[nombre].append({"codigo": codigo, "fecha prestamo": fechaPrestamo, "fecha devolucion": fechaDevolucion, "fecha entrega": fechaEntrega})
        endPrestec(codigo)
        print(diccIncidiencias)
        



def disponibilidad(codigo):
    """Esta función analiza la disponibilidad de los libros para sus prestamos"""
    if codigo not in diccLibros:
        print(f"Error, el libro con el código {codigo} no existe")
        return None
    else:
        if diccLibros[codigo]["disponibilitat"] == True:
            return True
        else:
            # print(f"Error, el libro con el codigo {codigo} no se encuentra disponible")
            return False

def fechaRetorno(codigo, fechaSalida):
    """esta función validará la fecha de entrega de los prestamos
        confirmando que la fecha de entrega es posterior a lña de entrada"""
    # codigo = listaComanda[1]
    fechaDevolucion = datetime.strptime(diccPrestamos[codigo]["fecha entrega"], "%Y/%m/%d")
    fechaEntrada = datetime.strptime(diccPrestamos[codigo]["fecha prestamo"], "%Y/%m/%d")
    fechaEntrega = datetime.strptime(fechaSalida, "%Y/%m/%d")

    if fechaEntrada < fechaEntrega:
        if fechaEntrega <= fechaDevolucion:
            print("Libro entregado en plazo. Procesando devolución...")
            return True
        else:
            print("El libro ha sido devuelto con retraso. Abriendo incidencia...  ")
            return False
    else:
        print("Error, la fecha de devolución debe ser posterior a la del prestamo")



# def fechaDevulición(fechaSalida, fechaRetorno):
    



# prueba = ["addLlibre","1234ab","pepe","Pedro","accion0","16"]
# prueba2 = ["addLlibre","1234abc","pepe","Pedro","accion0","16"]
# pruebaPrestamo = ["startprestec", "1234ab", "carlos", "12/02/2023"]
# pruebaPrestamo2 = ["startprestec","1234ab", "carlos", "12/02/2023"]


# print(diccLibrosStart(prueba))
# print(diccLibrosStart(prueba2))
# print(startPrestec(pruebaPrestamo))
# print(diccLibros[prueba[1]])
# print(startPrestec(pruebaPrestamo2))

# print(diccLibros)
