
print("Iniciando analisis de partido")  # Para empezar escribimos un print con la información del programa.
m = int(input("Introduce el numero de vicotrias del jugador 1: "))  # Solicitamos al usuario la primera varible, que será un número int.
if m >= 0 and m <= 8:   # Escribimos la primera sentencia alternativa en la cual establecemos las condiciones 0 <= m <= 8
    n = int(input("Introduce el numero de victorias del jugador 2: "))  # Si se cumple la sentencia, creamos la variable n y se la solicitamos al usuario.
    if n >= 0 and n <= 8:   # Anidamos la sentencia alternativa y analizamos si la varieble n ingresada por el usuario esta dentro del rango permitido, para ello usamos operadores de comparación y operadores lógicos.
        if m + n <= 13 and m - n <= 2 and n - m <= 2:   # Si la variable n es correcta, anidamos la siguiente sentencia, en la cual establecemos un límite, para n + m, acompañado del operador lógico and con la con la condición "n - m <= 2" y viceversa.
            if m == 6 and m == n + 2 or m == 7 and n == 6:  # Anidamos esta sentencia para las situaciones en las que gana el jugador 1, que son 2 argumentos, separados pro el comparador lógico "or", si "m = 6 and m = n +2" gana el jugador 1, o si "m = 7 and n = 6.
                print("Gana jugador 1") # Realizamos la impresion de los resultados
            elif n == 6 and n == m + 2 or n == 7 and m == 6:    # Realizamos el primsmo proceso que en el if anterior en esta sentencia, pero ahora con la variable n
                print("Gana el jugador 2")  # Imprimimos la victoria del jugador 2 en pantalla
            else:   # Este else tomará los valores que no cumplen las dos sentencias alternativas anteriores y cerrará el programa con una impresion.
                print("El juego aun no ha acabado") # Imprimimos en pantalla que el juego no ha acabado
        else:   # Este else cerrará el programa en caso de que no se cumplan las condiciones de la tercera sentencia alternativa.
            print("El resultado no es valido")  # Imprimimos en pantalla la invalidación.
    else:   # Construimos esta sentencia, que en caso de que "n", no sea un número valido, si no cumple el rango adecuado al ser introducido por el usuario
        print("Numero introducido incorrecto") # imprimimos en pantalla el error, y el programa terminará
else:   # Si no se cumple la primera sentencia alternativa, donde determinamos el rango de número permitido para "m", este else cerrará el programa
    print("Numero introducido incorrecto")  # Introducimos el error, y el programa terminará
