# Una empresa de publicitat vol posar tensió als anuncis posant punts suspensius, perquè
# un estudi científic indica que els punts suspensius donen tensió. No obstant, el responsable
# de Marketing, Marco Peloni, no sap de signes de puntuació així que els posa al tuntún.
# Fes un programa que llegeix una frase amb varies paraules i concateni punts suspensius
# “...” a cada paraula si aquesta és més curta que la paraula següent. No s’ha d’afegir mai
# punts a l’última paraula.

cantidadCasos = int(input("Introduce la cantidad de casos a considerar: ")) # Introducimos primera variable para considerar la cantidad de frases que introducirá el suuario a posterior
while cantidadCasos <= 0: # Error para casos menores a 0
    print("Error, introduce una cantidad de casos superior a 0")
    cantidadCasos = int(input("Introduce la cantidad de casos a considerar: "))  # Introducimos primera variable para considerar la cantidad de frases que introducirá el suuario a posterior

for i in range(cantidadCasos): #Primer for para introducir las frases del usuario
    frase = input("Introduce la frase para aplicar tensión: ") # Nueva variable, que es la frase del usuario
    palabras = frase.split(" ") # Creo una lista formada por las palabras en la frase introducidas por el usuario, en que cada elemento está separado por un espacio
    fraseNueva = "" # Creo una variable nueva para la frase nueva que generaré con los puntos suspensivos
    for j in range(len(palabras) - 1): # Bucle para determinar el total de los elementos de la lista, sin contar ell último
        if len(palabras[j]) < len(palabras[j + 1]): # Primera sentencia condicional dentro del bucle para que cuando la cantidad de letras de un elemento sea menor al siguiente sumemos puntos suspensivos
            fraseNueva += palabras[j] + "..." # Añadimos puntos suspensivos a las palabras que cumplan la condición
        else: # En caso de que no cumpla la condicion anterior, las añadiremos a la variable, pero sin puntos suspensivos
            fraseNueva += palabras[j] # Añadimos elemento a la variable
        fraseNueva += " " # Para añadir un espacio entre las palabras
    fraseNueva += palabras[-1] # Añadimos el último elemento de la lista, que no contemplamos en los casos anteriores
    print(fraseNueva) #Realizamos print final