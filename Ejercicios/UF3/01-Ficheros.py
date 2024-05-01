import os
import sys
# Esto es un ejemplo (por eso no hay funciones ni módulos)
# aplicación que registra notas de alumnos mediante
# línea de comandos
# uso fitxers.py nombre_alumno nota (para añadir alumno)
# uso fitxers.py list (para listar datos de los alumnos)

alumnos = {}
nombre_carpeta = "./pesados"
ruta_archivo = nombre_carpeta +"/notas.txt"
# si existe la carpeta
if os.path.exists(nombre_carpeta):
    # miramos si existe el fichero de datos
    if os.path.exists(ruta_archivo):
        # abrimos para leemos los datos
        f = open(ruta_archivo, "r")
        lineas = f.readlines()
        f.close()
        for linea in lineas:
            linea = linea.split("-")
            nombre = linea[0]
            nota = linea[1].replace("\n", "")
            nota = int(nota)
            alumnos[nombre] = nota
else:
    os.mkdir(nombre_carpeta)

comando = sys.argv
if len(comando) > 1:
    if len(comando) == 2:
        if comando[1].lower() == "list":
            #listado de alumnos
            if len(alumnos) == 0:
                print("No hay alumnos registrados")
            else:
                for nombre in alumnos:
                    print(nombre, "-", alumnos[nombre])
        else:
            print("Comando incorrecto")
    elif len(comando) == 3:
        nombre = comando[1]
        nota = int(comando[2])
        if nombre not in alumnos:
            #escribimos en el diccionario
            alumnos[nombre] = nota
            # escribimos en el fichero (con a para añadir)
            f = open(ruta_archivo, "a")
            f.write(nombre + "-" + str(nota) + "\n")
            f.close()
            print("Alumno registrado")
        else:
            print("Ya existe un alumno con ese nombre")
else:
    print("uso fitxers.py nombre_alumno nota (para añadir alumno)")
    print("uso fitxers.py list (para listar datos de los alumnos")