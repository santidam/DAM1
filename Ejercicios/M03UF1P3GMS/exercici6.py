acabar = True # Boolean para iniciar bucle
lista = [] # Creamos lista fuera del bucle
while acabar == True: # Mientras acabar sea True, el bucle continuará, con esto nos aseguramos de que el bucle solo acabe cuando el usuario así lo desee
    print(f"Menu: \n" # Escribimos el menu para el usuario
          f"1. Añadir \n"
          f"2. Contar \n"
          f"3. Modificar \n"
          f"4. Eliminar \n"
          f"5. Mostrar palabras \n"
          f"6. Acabar")
    orden = input("Introduce tu orden: ") # Solicitamos la orden del usuario sobre el menu
    if orden == "1": # opcion 1 añadir
        print("Has escogido la opción añadir")
        añadir = input("Introduce una palabra para añadir a la lista: ") #Solicitamos el elemento para añadir al usuario
        lista.append(añadir) # Añadir elemento a la lista
        print(f"Has añadido {añadir} a la lista") # Informamos al usuario del elemento añadido
    elif orden == "2": # Opcion 2 del menu, contar
        if not lista: # Si la lista esta vacia, imprimimos error
            print(f"Error, la lista está vacia")
        else: # Si la lista tiene elementos
            print("Has escogido la opción contar")
            contar = input("Introduce una palabra para saber cuantas veces se repite en la lista: ") # Elemento a contar
            if contar in lista: # Si el elemento que el usuario desea contar está en la lista procedemos
                print(f"La palabra {contar} se repite: {lista.count(contar)} vez") # Informamos al usuario de las repeticiones de dicho elemento
            elif contar not in lista: # Si el elemento no está en la lista
                print(f"Error, el elemento {contar} no se encuentra en a lista") # Informamos del error
    elif orden == "3": # Menu 3 Modificar
        if not lista: # Si la lista está vacía
            print(f"Error, la lista está vacia") # Informamos del error
        else: # Si la lista tiene elementos
            print("Has escogido la opción modificar")
            cadena = input("Introduce la cadena a modificar: ") # Elemento que el usuario quiere sustituir
            if cadena in lista: # Si el elemento que el usuario quiere modificar está en la lista, procedemos
                cadena2 = input("Introduce la modificación: ") # Elemento que el usuario quiere en la lista
                for j in range(len(lista)): # Bucle en el que determinamos los elementos de la lista
                    if lista[j] == cadena: # Si el elemento es igual al que queremos modificar
                        lista[j] = cadena2 # Lo reemplazamos
            elif cadena not in lista: # Si el elemento no esta en la lista
                print(f"Error el elemento {cadena} no se encuentra en la lista") # informamos del error
        print() # Salto de línea
    elif orden == "4": # Orden eliminar
        if not lista: # Si la lista está vacía, indicamos error
            print(f"Error, la lista está vacia")
        else: # Sino prodecemos
            print("Has escogido la opción eliminar")
            eliminar = input("Introduce el elemento que quieres eliminar: ") # Pedimos elemento que deseamos evitar
            if eliminar in lista: # Si el elemento que queremos eliminar está en la lista
                while eliminar in lista: # Mientras el elemento que queremos liminar esté en la lista el bucle continuará
                    lista.remove(eliminar) # Eliminamos el elemento de la lista
                print(f"Elemento {eliminar} eliminado de la lista") # Confirmamos al usuario la eliminación del elemento
            elif eliminar not in lista: # Si el elemento no está en la lista
                print(f"Error, el elemento {eliminar} no se encuentra en la lista") # Informamos del error
    elif orden == "5": # Menu mostrar palabras
        print("Has escogido mostrar palabras")
        if not lista: # Si la lista está vacía
            print(f"Error, la lista está vacia") # Informamos error
        else: # Si la lista tiene elementos
            for i in lista: # Bucle for donde iteramos los elementos de la lista para realizar print de ellos
                print(i, end="\t") # Impresión de de los elementos en la misma línea con tabulación
            print() # Elemento
    elif orden == "6": # Opción menu para cerrar programa
        print("Has escogido acabar")
        acabar = False # Variable acabar se convierte en False para cerrar bucle
    else: # Si el usuario introduce un carcater que no sea valido para el menu mostramos error
         print(f"Error, no has introducido un comando invalido")



