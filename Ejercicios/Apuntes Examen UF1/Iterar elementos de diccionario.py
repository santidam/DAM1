diccionario= {}
diccionario["a"] = {"x": 1, "z": 2}
personaje = "pepe"
for x, y in diccionario.items(): # Iteramos con el bucle for "X" que viene a ser el nombre principal del diccionario. y "Y" que son los elementos con string dentro del diccionario
    if x.lower() == personaje: # .tems() nos da una lista con toda las llaves y valores del diccionario
        print(f"Nombre : {x.capitalize()}")
        for n, d in y.items():
            print(f"{n} : {d}", end="\t")
        print()