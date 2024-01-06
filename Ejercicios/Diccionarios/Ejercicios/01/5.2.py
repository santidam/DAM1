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
        if nombre in diccionario:
            print(f"Error, ya existe un personaje con ese nombre\n"
                  f"Volviendo al menu principal")
        else:
            fuerza = int(input("Introduce la fuerza del personaje: "))
            if fuerza < 0:
                print(f"Error, has introducido un valor de fuerza negativo\n"
                      f"Volviendo al menu principal")
            else:
                print("FUERZA OK")
                resistencia = int(input("Introduce la resistencia del personaje: "))
                if resistencia < 0:
                    print(f"Error, has introducido una valor de resistencia negativo\n"
                          "Volviendo al menu principal")
                else:
                    print("RESISTENCIA OK")
                    vida = int(input("Introduce la vida del personaje: "))
                    if vida <= 0:
                        print(f"Error, has introducido un valor de vida igual o menor a 0\n"
                              f"Volvindo al mnu principal")
                    else:
                        print("VIDA OK")
                        tipo = input("Introduce el tipo de personaje, guerrero o mago: ").lower()
                        if tipo != "guerrero" and tipo != "mago":
                            print(f"Error, no has introducido el tipo correcto\n"
                                  f"Volviendo al menu principal ")
                        else:
                            if tipo == "guerrero":
                                print("TIPO GUERRERO OK")
                                armadura = int(input("Introduce el valor de la armadura: "))
                                if armadura < 0:
                                    print("Error, has introducido un valor negativo de armadura")
                                    print("Volviendo al menu principal")
                                else:
                                    print("ARMADURA OK")
                                    diccionario[nombre] = {"Fuerza": fuerza, "Resistencia": resistencia,"Vida": vida, "Tipo": tipo, "Armadura": armadura}
                            else:
                                print("TIPO MAGO OK")
                                mana = int(input("Introduce el valor del mana: "))
                                if mana < 0:
                                    print("Error, has introducido un valor negativo de mana")
                                    print("Volviendo al menu principal")
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
        print("Has escogido la opción mostrar personaje")
        personaje = input("Introduce el personaje que quieres mostrar: ").lower()
        if personaje not in diccionario:
            print(f"Error el personaje introducido no está en la lista\n"
                  f"Volviendo al menu principal")
        else:
            print("_"*1000)
            print(f"Nombre: {personaje}\n"
                  f" {diccionario[personaje]}")
            print("_"*1000)
    elif usuario == "4":
        print("Has seleccionado mostrar todos los personajes")
        if not diccionario:
            print("Error no hay personajes guardados")
        else:
            print("_" * 1000)
            for i in diccionario:
                print(f"Nombre : {i}")
                print(diccionario[i])
                print("_" * 1000)
    elif usuario == "5":
        print("Has escogido la opción mostrar personajes por tipo")
        personaje = input("Introduce Guerrero o Mago para mostrar: ").lower()
        if personaje == "guerrero":
            print("_" * 1000)
            for i in diccionario:
                if diccionario[i]["Tipo"] == "guerrero":
                    print(f"Nombre: {i}\n"
                          f"{diccionario[i]}")
                    print("_" * 1000)
        elif personaje == "mago":
            print("_" * 1000)
            for i in diccionario:
                if diccionario[i]["Tipo"] == "mago":
                    print(f"Nombre: {i}\n"
                          f"{diccionario[i]}")
                    print("_" * 1000)
        else:
             print(f"Error, el tipo de personaje introducido es incorrecto\n"
                   f"Volviendo al menu principal")
    elif usuario == "6":
        print(f"Has seleccionado salir\n"
              f"Adios")
        salir = False
    else:
        print("Error, no has introducido un comando valido")