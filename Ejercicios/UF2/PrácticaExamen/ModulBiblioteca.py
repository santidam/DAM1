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
        será 15 días despues, agregando esta informacion en el diccionario de Prestamos y de Libros"""


    diccPrestamos[listaComanda[1]] = {
        "Alumno": listaComanda[2], "fecha prestamo": fechaInicio, "fecha entrega": fechaFinal}
    diccLibros[listaComanda[1]]["disponibilitat"] = False

    return f"Prestamo realizado. El libro se debe entregar el {fechaFinal}"

def endPrestec(codigo):
    """Esta función finaliza un préstamo que haya sido entregado en un tiempo dentro del rango del prestamo, cambiando la disponiblidad del libro y quitando el libro
        del diccionario de Prestamos"""
    diccLibros[codigo]["disponibilitat"] =  True
    del diccPrestamos[codigo]
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

def List(tipo, genero):
    """Esta función genera una lista de los diccionarios según la entrada proporcionada, siendo el primer parámetro introducido
        el que determina que lista mostrará, y el segundo, solo es necesario para la lista genero. """
    if tipo == "llibres":
        for x in diccLibros:
            print(x,":", diccLibros[x]["titulo"],",", diccLibros[x]["autor"],"- ESTAT:", diccLibros[x]["disponibilitat"])
    elif tipo == "prestec":
        if not diccPrestamos:
            print("Actualmente no hay libros en prestamo")
        else:
            for x in diccPrestamos:
                print("Llibre:",x,": Alumne:", diccPrestamos[x]["Alumno"],"Data inici:", diccPrestamos[x]["fecha prestamo"],"Data fi:", diccPrestamos[x]["fecha entrega"])

    elif tipo == "genere":
        contadorGenero = 0
        for x in diccLibros:
            if diccLibros[x]["genero"] == genero:
                contadorGenero += 1
                print(x,":", diccLibros[x]["titulo"],",", diccLibros[x]["autor"],"- ESTAT:", diccLibros[x]["disponibilitat"])
        if contadorGenero == 0:
            print("Error, no existen libros del genero seleciconado")
def maxllibre():
    "Esta función analiza las páginas de los libros que se encuentran en el diciconario de Libros y determina cúal tiene más páginas"
    
    contador = 0
    max = None
    for x in diccLibros:
        if int(diccLibros[x]["paginas"]) > contador:
            contador = int(diccLibros[x]["paginas"])
            max = x
    print("El llibre amb més pàgines de la biblioteca és:",diccLibros[max]["titulo"],f" amb {contador} pàgines")

def stats():
    """esta función estudia la cantidad de libros en la biblioteca, la cantidad de incidencias y la media de las páginas de todos los libros"""
    contadorLibros = len(diccLibros)
    contadorIncidencias = 0
    contadorPáginas = 0

    for x in diccLibros:
        contadorPáginas += int(diccLibros[x]["paginas"])
    for x in diccIncidiencias:
        contadorIncidencias += len(diccIncidiencias[x])

    print(f"Número de llibres registrats: {contadorLibros}")
    print(f"Número d'incidències registrades:{contadorIncidencias}")
    print(f"Mitjana de pàgines per llibre: {contadorPáginas/contadorLibros}")        

def info(nombre):
    """Esta función proporciona datos relativos a los prestamos y incidencias del nombre proporcionado en la base de datos"""
    
    print("Llibres en préstec")
    contadorPrestamo = 0
    for x in diccPrestamos:
        if diccPrestamos[x]["Alumno"] == nombre:
            contadorPrestamo += 1
            print("Llibre:", x,"- ",diccLibros[x]["titulo"], "Inici:", diccPrestamos[x]["fecha prestamo"], "Data fi:",diccPrestamos[x]["fecha entrega"])
    if contadorPrestamo == 0:
        print("L'alumne indicat no té cap llibre en préstec.")
    print("Incidencias:")

    if nombre not in diccIncidiencias:
        print(f"El alumno { nombre} no tiene incidencias registradas")
    else:
        
        for i in range(len(diccIncidiencias["pepe"])):
            print("Llibre:", diccIncidiencias["pepe"][i]["codigo"]," Data Inici Préstec:", diccIncidiencias["pepe"][i]["fecha prestamo"], "Data Fi:", diccIncidiencias["pepe"][i]["fecha devolucion"], "Data Retorn:", diccIncidiencias["pepe"][i]["fecha entrega"])
        # print(f"El alumno tiene {len(diccIncidiencias[nombre])}")

def validarDiccLibros():
    """Esta funcion determina la existencia de elementos en el diccionario principal de libros
        y devuelve un Booleano para cada situación"""
    if not diccLibros:
        print("Error, no existen libros en la base de datos")
        return False
    return True

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
        confirmando que la fecha de entrega es posterior a la de entrada"""
    # codigo = listaComanda[1]
    fechaDevolucion = datetime.strptime(diccPrestamos[codigo]["fecha entrega"], "%Y/%m/%d")
    fechaEntrada = datetime.strptime(diccPrestamos[codigo]["fecha prestamo"], "%Y/%m/%d")
    fechaEntrega = datetime.strptime(fechaSalida, "%Y/%m/%d")

    if fechaEntrada <= fechaEntrega:
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

# diccLibros = {"001":{"titulo": "Titulo1", "autor": "Autor1","genero": "genero1", "paginas": 600, "disponibilitat": False, "fechaEntrega": "2024/02/13"}, 
#               "002": {"titulo": "Titulo1", "autor": "Autor1","genero": "genero1", "paginas": 400, "disponibilitat": False, "fechaEntrega": "2024/02/13"},
#               "003": {"titulo": "Titulo1", "autor": "Autor1","genero": "genero2", "paginas": 300, "disponibilitat": False, "fechaEntrega": "2024/02/13"},
#                "004": {"titulo": "Titulo1", "autor": "Autor1","genero": "genero2", "paginas": 550, "disponibilitat": True, "fechaEntrega": None}}
# diccPrestamos = {"001":{"Alumno": "alumno1", "fecha prestamo": "2024/01/30","fecha entrega": "2024/02/13"}, 
#               "002": {"Alumno": "alumno2", "fecha prestamo": "2024/01/30","fecha entrega": "2024/02/13"},
#               "003": {"Alumno": "alumno3", "fecha prestamo": "2024/01/30","fecha entrega": "2024/02/13"}}
# List("llibres", "no")
# List("prestec", "no")
# print(len(diccLibros))