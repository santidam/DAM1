# 1) Crea un programa que le pida un número entero al usuario y cree un triángulo rectángulo:
x = int(input("introduce un número: ")) # Usuario introduce variable entera
for i in range(1, x + 1): # Construimos una iteración "i" en el rango n + 1
    print(i * "*") # Realizamos la impresión en pantalla, multiplicando cada iteración por el string "*".

# 2) Escribe un programa que pida al usuario un número entero y muestre un tríángulo rectángulo inverso:
y = int(input("Introduce un número: ")) # Construimos variable entera
for n in range(y + 1): # creamos primera iteración n en rango y + 1 que determinará la altura
    for x in range(y - n): # En esta línea estamos creando los espacios del principio de línea, para esto restamos y - n, donde y viene siendo el número entero y n la iteración
        print(" ", end="") # Imprimimos los espacios, y señalamos el final que cada iteracion acabe al final de la línea con end="" para no ocurra un salto de línea en cada espacio
    for k in range(n):  # El tercer for determina los asteriscos del triángulo, por lo tanto, estan construidos con la variable n
        print("*", end="")
    print() # al realizar el cada bucle, este print genera un salto de línea entre cada iteración
# 3) Construye un triángulo isosceles con el número entero entregado por el usuario

for n in range(y + 1): # For que determina la altura
    for x in range( y - n): # Segundo for para ddeterminar los espacios antes de los asteriscos
        print(" ", end="") # print de espacios por cada iteracion + su valor. el end al final es para que acabe la línea
    for k in range(n):  # Este k en el rango n construye la primera parte del triángulo con asteriscos
        print("*", end="")  # Este print hace que cada iteración se convierta junto a su valor en asteriscos, el end hace que no cambie de línea por cada iteración
    for j in range(2, n + 1): # Para este cuarto for creamos la variable j que estará en el rango 2, n +1. haciendo que comience en la iteración 2, y aplicando el valor de n + 1 en cada línea
        print("*", end="")  # convertimos en asteriscos las iteraciones y hacemos que vayan hasta el final de la línea.

    print() # Cambio de línea al terminar cada bucle,

# 4) En el trángulo anterior construyelo de tal manera que en cada línea par aparezca una "o", centradas en líneas pares y cada 3 asteriscos

for n in range(y + 1):
    for x in range(y - n):
        print(" ", end="")
    for k in range(n):
        print("*", end="")
        if n % 2 == 0:
            for k in range(n):
                print("o" , end="")
    for j in range(2, n + 1):
        print("*", end="")
    print()
