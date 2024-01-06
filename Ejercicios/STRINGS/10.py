x = input("Quieres salir? ")
while x.lower() != "si":
    if x.isnumeric() == True:
        x = input("Error, has introducido números, responde si o no : ")
    elif x == "":
        x = input("Error, no has introducido nada: ")
    elif x.lower() == "no":
        x = input("No quieres salir, quieres salir ahora? ")
    elif x.isalpha() == True:
        x = input("Error, has introducido otra palabra, responde si o no : ")
    elif x.isspace() == True:
        x = input("Error, solo has introducido espacios, quieres salir?")
    elif x.isalnum() == True:
        x = input("Error, has introducido un código alfanúmerico, responde si o no : ")
    else:
        x = input("Error no has dicho ni si ni no, responde si o no ")
print("Estás fuera")
