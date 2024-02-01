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
        print("Usuario introducido correctamente")
        if len(clave) >= 6:
            vocales = "aeiouAEIOU"
            for i in clave:
                if i in vocales:
                    print("Contraseña introcida correctamente")
                    return True
                else:
                    print("Error la contraseña debe contener al menos una vocal")
                    return False
        else:
            print("Error: La contraseña introducida debe tener 6 o más caracteres")
            return False
