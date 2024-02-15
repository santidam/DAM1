def validar_negativo(dato):
    """Función para validar si el valor ingresado es negativo retorna True si es negativo y False en caso contrario """
    if dato.count("-") == 1 and dato[0] == "-":
        dato = dato.split("-")
        if dato[1].isdigit() == True:
            return True
        else:
            return False
    else:
        return False
print(validar_negativo("-b"))