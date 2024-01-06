salir = True
diccionario = {}
while salir == True:
    print(f"*** Expediente academico ***\n"
          f"1. Alta de modulo\n"
          f"2. Alta de una nota de una unidad formativa de un modulo\n"
          f"3. Ver datos de un modulo\n"
          f"4. Ver el % de unidades formativas aprobadas\n"
          f"5. Salir")
    opcion = input("Selecciona una opción para continuar: ")
    if opcion == "1": # Alta modulo
        print("Has seleccionado dar de alta un módulo")
        altaModulo = input("Introduce el modulo deseas dar de alta: ").lower()
        while altaModulo in diccionario:
            print("Error el modulo introducido ya se encuentra en el diccionario")
            altaModulo = input("Introduce otro modulo para continuar: ").lower()
        else:
            print("Alta modulo OK")
            diccionario[altaModulo] = {}
    elif opcion == "2": # Alta nota UF de modulo
        print("Has seleccionado dar de alta una nota de una UF de  un modulo")
        if not diccionario:
            print("Error no hay ningun modulo registrado\n"
                  "Volviendo al menu principal")
        else:
            modulo = input("Introduce el nombre del modulo: ").lower()
            while modulo not in diccionario:
                print("Error, el modulo seleccionado no se encuentra registrado")
                modulo = input("Selecciona otro modulo: ").lower()
            else:
                print("MODULO OK")
                unidadFormativa = input("Introduce el nombre de la Unidad Formativa: ").lower()
                if unidadFormativa in diccionario[modulo]:
                    print("Error, ya hay una nota registrada para la unidad formativa indicada")
                    print("Volviendo al menu principal")
                else:
                    print("Creando unidad formativa OK")
                    nota = int(input("Introduce una nota entre 1 y 10 para la Unidad Formativa seleccionada: "))
                    while nota < 1 or nota > 10:
                        print("Error, nota introducida fuera de rango")
                        nota = int(input("Introduce una nota entre 1 y 10, estos incluidos para continuar: "))
                    else:
                        print("NOTA OK")
                        print(f"Nota: {nota} introducida de Unidad Formativa {unidadFormativa} del modulo {modulo}")
                        diccionario2 = {}
                        diccionario2[modulo] = {unidadFormativa : nota}
                        diccionario[modulo].update(diccionario2[modulo])
    elif opcion == "3": # Datos de modulo
        print("Has seleccionado la opción mostrar datos de un modulo")
        if not diccionario:
            print("Error, no hay ningún modulo registrado ")
        else:
            modulo = input("Introduce el nombre del módulo: ").lower()
            if not diccionario[modulo]:
                print(f"Error no hay elementos en el modulo {modulo.capitalize()}")
                print("Volviendo al menu principal")
            else:
                while modulo not in diccionario:
                    print("Error, el modulo introducido no se encuentra registrado")
                    modulo = input("Introduce otro modulo para continuar: ").lower()
                else:
                    suma = 0
                    aprobado = True
                    print("MODULO OK")
                    print(f"Modulo: {modulo.upper()}")
                    print(f"Numero de unidades formativas registradas: {len(diccionario[modulo])}")
                    for x, y in diccionario.items():
                        if x == modulo:
                            for i, j in y.items():
                                print(f"{i.capitalize()} : {j}")
                                suma += j
                                if j < 5:
                                    aprobado = False
                            if aprobado == True:
                                print("Nota media del modulo:", suma//len(diccionario[modulo]))
    elif opcion == "4": # % de aprobación
        print("Has seleccionado la opción mostrar el porcentaje de UFs aprobadas")
        if not diccionario:
            print("Error, no hay ningun modulo registrado ")
        else:
            elementos = False
            for k in diccionario:
                if len(diccionario[k]) > 0:
                    elementos = True
            if elementos == False:
                print("Error, no existen Notas en los modulos")
            else:
                sumaAprobados = 0
                sumaTotal = 0
                for x, y in diccionario.items():
                    for i, j in y.items():
                        if j >= 5:
                            sumaTotal += 1
                            sumaAprobados += 1
                        else:
                            sumaTotal += 1
                print(f"El porcentaje de Unidades Formativas aprobadas en todo el expediente es: {(sumaAprobados/sumaTotal) * 100}")
    elif opcion == "5": # Salir
        print("Has seleccionado salir")
        print("Cerrando sistema")
        salir = False
    else:
        print("Error, no has introducido una opción valida")


