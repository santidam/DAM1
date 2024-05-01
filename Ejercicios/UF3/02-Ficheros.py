import os
import sys

alumnos = {}
nombre_carpeta = "pesados"
ruta_archivos = nombre_carpeta +"/notas.txt"

#Si existe la cartpeta:

if os.path.exists(nombre_carpeta):
    # miramos si existe fichero
    if os.path.exists(ruta_archivos):
        # Abrimos para leer los datos
        f = open(ruta_archivos, "r")
        lineas = f.readlines()
        f.close()
        # Leemos linea por linea y creamos variables que nos interesan de la lectura
        # que realizamos
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
            # listado de alumnos
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
            # Escribirmos en el diccionario
            alumnos[nombre] = nota
else:
    print("Error: añadir nombre y nota alumno ")