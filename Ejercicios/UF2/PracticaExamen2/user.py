diccUsuario = {}
def DemanarEdat():
    """Esta función pide al usuario una edad y valida que este entre 0 y 130.
        Si no es correcto seguirá pdidiendo la edat hasta que sea correcto, hace retorn de la edat"""

    salir = False
    while salir == False:
        edat = input("Introduce una edat entre 0 y 130: ")
        if edat.isdigit() is True:
            if int(edat) >= 0 and int(edat) <= 130:
                print("Eedat introducida corerctamente")
                salir = True
                return edat
            else:
                print("Error, el número introducido esta fuera de rango")
        else:
            print("Error no has introducido un carácter valido")


def validarUsuari(usuario, clave):
    if len(usuario) >= 4:
        print("Nombre de usuario introducido correctamente")
        if disponibilidadUsuario(usuario) == True:
            if len(clave) >= 6:
                vocales = "aeiouAEIOU"
                contador = 0
                for i in clave:
                    if i in vocales:
                        contador += 1
                if contador == 0:
                    print("Error la contraseña debe contener al menos una vocal")
                    return False          
                else:
                    print("Contraseña introducida correctamente")
                    return True
            else:
                print("Error: La contraseña introducida debe tener 6 o más caracteres")
                return False
        else:
            return False
    else:
        print("Error: el nombre de usuario debe tener al menos 4 carácteres")
        return False
def registrarUsuario(usuario , clave):
    """Esta función registra al usuario en la base de datos"""
    if validarUsuari(usuario, clave) == True:
        edat = DemanarEdat()
        diccUsuario[usuario] = {"contraseña": clave, "edat": edat }
        print("Usuario registrado correctamente")


def disponibilidadUsuario(usuari):
    """Esta función comprueba la disponibilidad del nombre del usuario en el a base de datos"""
    if usuari in diccUsuario:
        print("Error: el nombre de usuario no se encuentra disponible")
        return False
    else:
        return True