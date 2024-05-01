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
    """La funció rep dos paràmetres, usuari i clau i ha de validar que siguin correctes.
        Un usuari és correcte si té almenys 4 caràcters i la clau és correcte si té 6 caràcters i té al menys una vocal.
        Retorna un booleà indicant si el usuari i la clau compleix el requisit.  """
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

def demanarNaixement():
    """ aquesta funció ha de demanar a lusuari la data de naixement demanant tres dades:
        - dia: ha de ser un número entre 1 i 31.
        - mes: ha de ser un número entre 1 i 12.  
        - any: ha de ser un número entre 1900 i 2021. 
        La funció retornarà una cadena amb el format “dia/mes/any”. 
        Per simplificar només es faran les comprovacions que indica lenunciat.  """
    
    salirDia = False
    while salirDia == False:
        dia = input("Introduce una dia entre 1 y 31: ")
        if dia.isdigit() is True:
            if int(dia) >= 1 and int(dia) <= 31:
                print("Dia introducido corerctamente")
                salirDia = True
            else:
                print("Error, el número introducido esta fuera de rango")
        else:
            print("Error no has introducido un carácter valido")
    
    salirMes = False
    while salirMes == False:
        mes = input("Introduce una dia entre 1 y 12: ")
        if mes.isdigit() is True:
            if int(mes) >= 1 and int(mes) <= 12:
                print("Mes introducido corerctamente")
                salirMes = True
            else:
                print("Error, el número introducido esta fuera de rango")
        else:
            print("Error no has introducido un carácter valido")
    
    salirYear = False
    while salirYear == False:
        year = input("Introduce una dia entre 1900 y 2021: ")
        if year.isdigit() is True:
            if int(year) >= 1900 and int(year) <= 2021:
                print("Año introducido corerctamente")
                salirYear = True
            else:
                print("Error, el número introducido esta fuera de rango")
        else:
            print("Error no has introducido un carácter valido")
    return f"{dia}/{mes}/{year}"

def login(dicc, usuario, clave):
    if usuario in dicc:
        if dicc[usuario]["contraseña"] == clave:
            print("Usuario y claves introducidos correctos")
            return True
        else:
            print("Error: Contraseña introducida incorrecta")
            return False
    else:
        print("Error: El usuario introducido no se encuentra registrado")
        return False
