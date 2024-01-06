nombres = []
edades = []
mayor = 0
alumnomayor = []
alumnos = input("Introduce el nombre y la edad: ")
while alumnos != "*":
    nombresEdades = alumnos.split(" ")

    if nombresEdades != "*":
        nombre = nombresEdades[0]
        edad = int(nombresEdades[1])
        if edad >= 18:
        nombres.append(nombre)
        edades.append(edad)
        elif edad >= mayor:
            mayor = edad
            alumnomayor.append(nombre)
            alumnomayor.append((edad))
    alumnos = input("Introduce el nombre y la edad: ")
for i in range(len(nombres)):
    print(f"Nombre: {nombres[i]}, edad: {edades[i]}")
print(f"Alumno mayor: {alumnomayor[-2]} {alumnomayor[-1]} años")

#Arreglar proteccion de * y 0