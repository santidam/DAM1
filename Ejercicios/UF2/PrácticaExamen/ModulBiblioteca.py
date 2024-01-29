# En este módulo se almacenarán las bases de datos del programa, siendo accesibles
# desde el módulo interpret
# import ModulInterpret as mi
from datetime import datetime

diccLibros = {}  # diccionario de libros
diccAlumnos = {}  # diccionarios de alumnos con prestamos


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
    # if listaComanda[1] not in diccLibros:
    #     return f"Error, el libro con el código {listaComanda[1]} no existe"
    # else:
    # if diccLibros[listaComanda[1]]["disponibilitat"] == False:

    diccAlumnos[listaComanda[2]] = {
        "codigo": listaComanda[1], "fecha prestamo": fechaInicio, "fecha entrega": fechaFinal}
    diccLibros[listaComanda[1]]["disponibilitat"] = False

    return f"Prestamo realizado. El libro se debe entregar el {fechaFinal}"


def disponibilidad(codigo):
    """Esta función analiza la disponibilidad de los libros para sus prestamos"""
    if codigo not in diccLibros:
        return f"Error, el libro con el código {codigo} no existe"
    else:
        if diccLibros[codigo]["disponibilitat"] == True:
            return True
        else:
            return False


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
