def demanarEdad(num1):
    while num1 <= 0 or num1 > 130:
        num1 = int(input("Error, introduce una edad valida entre 0 y 130 años: "))
    return num1
def validarUsuari(usuario, clave):
    valido =  False
    vocales = "aeiouAEIOU"
    if len(usuario) >= 4 and len(clave) == 6 and vocales in clave:
        valido = True
    return valido
usuario = input("Introduce el nombre del ususario: ")
clave = input("Introduce la contraseña: ")
print(validarUsuari(usuario, clave))


def demanarNaixement():
    dia = int(input("introduce el día de nacimiento, debe ser entre 1 y 31: "))
    while 1 < dia > 31:
        dia = int(input("Error, no has introducido un número dentro del rango, vuelve a introducirlo: "))
    mes = int(input("introduce el mes de nacimiento, debe ser entre 1 y 12: "))
    while 1 < mes > 12:
        mes = int(input("Error, no has introducido un número dentro del rango, vuelve a introducirlo: "))
    año = int(input("introduce el año de nacimiento, debe ser entre 1900 y 2021: "))
    while 1900 < año > 2021:
        dia = int(input("Error, no has introducido un número dentro del rango, vuelve a introducirlo: "))
    cadenaFecha = f"{dia}/{mes}/{año}"
    return cadenaFecha
def login(diccionario):
    validacion = False
    for x, y in diccionario.items():
        if x == usuario and y == clave:
            validacion = True
    return validacion
