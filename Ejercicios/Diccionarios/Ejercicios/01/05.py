# Escriu un programa que permeti gestionar els personatges d’un joc de rol.
# Els personatges es guardaran a un diccionari on la clau serà el nom, i el
# valor serà un altre diccionari on es guardarà la força, resistència i vida (que
# seran enters), tipus de personatge (que pot ser guerrer o mag). En cas de
# ser guerrer s’emmagatzemarà un enter que serà el valor de la seva
# armadura, i si es mag s’haurà de demanar un enter que correspondrà al
# seu manà.

diccionario = {}
salir = True
while salir == True:
    print(f"1) Añadir personaje\n"
          f"2) Borrar personaje\n"
          f"3) Mostrar personaje\n"
          f"4) Mostrar todos los dados de todos los personajes\n"
          f"5) Mostrar los datos de un tipo de personaje\n"
          f"6) Salir")
    usuario = input("Introduce un comando: ")
    if usuario == "1":
        print("Has seleccionado, añadir personaje")
        nombre = input("Introduce el nombre del personaje: ").lower()
        while nombre in diccionario:
            print(f"Error, ya existe un personaje con ese nombre")
            nombre = input("Introduce otro nombre para el personaje: ").lower()
        else:
            print("NOMBRE OK")
            fuerza = int(input("Introduce la fuerza del personaje: "))
            while fuerza <= 0:
                print(f"Error, has introducido un valor de menor a 1")
                fuerza = int(input("Vuelve a introducir la fuerza del personaje: "))
            else:
                print("FUERZA OK")
                resistencia = int(input("Introduce la resistencia del personaje: "))
                while resistencia <= 0:
                    print(f"Error, has introducido una valor de resistencia negativo")
                    resistencia = int(input("Vuelve a introducir la resistencia del personaje: "))
                else:
                    print("RESISTENCIA OK")
                    vida = int(input("Introduce la vida del personaje: "))
                    while vida <= 0:
                        print(f"Error, has introducido un valor de vida menor a 1")
                        vida = int(input("Vuelve a introducir la vida del personaje: "))
                    else:
                        print("VIDA OK")
                        tipo = input("Introduce el tipo de personaje, guerrero o mago: ").lower()
                        while tipo != "guerrero" and tipo != "mago":
                            print(f"Error, no has introducido el tipo correcto")
                            tipo = input("Vuelve a introducir el tipo de personaje, guerrero o mago: ").lower()
                        else:
                            if tipo == "guerrero":
                                print("TIPO GUERRERO OK")
                                armadura = int(input("Introduce el valor de la armadura: "))
                                while armadura < 0:
                                    print("Error, has introducido un valor menor a 1 de armadura")
                                    armadura = int(input("Vuelve a introducir el valor de la armadura: "))
                                else:
                                    print("ARMADURA OK")
                                    diccionario[nombre] = {"Fuerza": fuerza, "Resistencia": resistencia,"Vida": vida, "Tipo": tipo, "Armadura": armadura}
                            else:
                                print("TIPO MAGO OK")
                                mana = int(input("Introduce el valor del mana: "))
                                while mana < 1:
                                    print("Error, has introducido un valor menor a 1 de mana")
                                    mana = int(input("Introduce el valor del mana: "))
                                else:
                                    print("MANA OK")
                                    diccionario[nombre] = {"Fuerza": fuerza, "Resistencia": resistencia,"Vida": vida, "Tipo": tipo, "Mana": mana}
                                    print(f"Personaje {nombre} creado correctamente")
    elif usuario == "2":
        print("Has seleccionado borrar personaje")
        personaje = input("Introduce el nombre del personaje que deseas eliminar: ")
        if personaje not in diccionario:
            print(f"Error, el personaje introducido no se encuentra en la lista\n"
                  f"Volviendo al menu principal")
        else:
            diccionario.__delitem__(personaje)
            print(f"Personaje {personaje} ha sido eliminado correctamente")
    elif usuario == "3":
        # sin llaves: for i in diccionario[personaje]
        #               print(i, personaje[nombre][i]
        print("Has escogido la opción mostrar personaje")
        personaje = input("Introduce el personaje que quieres mostrar: ").lower()
        if personaje not in diccionario:
            print(f"Error el personaje introducido no está en la lista\n"
                  f"Volviendo al menu principal")
        else:
            print("_"*1000)
            for x, y in diccionario.items():
                if x.lower() == personaje:
                    print(f"Nombre : {x.capitalize()}")
                    for n, d in y.items():
                        print(f"{n} : {d}", end="\t")
                    print()
                    print("_" * 1000)
    elif usuario == "4": # Mostrar todos los personajes
        print("Has seleccionado mostrar todos los personajes")
        if not diccionario:
            print("Error no hay personajes guardados")
        else:
            print("_" * 1000)
            for x, y in diccionario.items():
                   print("Nombre:", x.capitalize())
                   for n, d in y.items():
                       print(n, ":", d, end="\t")
                   print()
                   print("_" * 1000)
    elif usuario == "5": # Mostrat personajes por tipo
        print("Has escogido la opción mostrar personajes por tipo")
        personaje = input("Introduce Guerrero o Mago para mostrar: ").lower()
        if personaje != "guerrero" and personaje != "mago":
            print(f"Error, el tipo de personaje introducido es incorrecto\n"
                  f"Volviendo al menu principal")
        else:
            print("_" * 1000)
            for x, y in diccionario.items():
                if y["Tipo"].lower() == personaje:
                    print("Nombre: ", x.capitalize())
                    for n , d in y.items():
                        print(f"{n} : {d}", end="\t")
                    print()
                    print("_" * 1000)

    elif usuario == "6":
        print(f"Has seleccionado salir\n"
              f"Adios")
        salir = False
    else:
        print("Error, no has introducido un comando valido")