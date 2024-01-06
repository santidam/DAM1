#  1) Imprimir els números entre el 5 i el 20, saltant de tres en tres
print("Numeros entre el 5 y el 10 de 3 en 3: ")
for numero in range(5,21,3):
    print(numero)
#  2)  Requerir a l'usuari que ingressi un nombre enter positiu i imprimir tots
# els números correlatius entre l'ingressat per l'usuari i un menys del doble
# d'aquest.
print("Iniciando numeros correlativos hasta el doble menos 1")
n = int(input("Ingresa un número entero positivo: "))
if n > 0:
    for i in range(n, 2 * n):
        print(i)
else:
    while n < 0:
        n = int(input("Ingresa un número valido: "))


# 3) Escriure un programa que mostri la sumatòria de tots els números entre
# el 0 i el 100.

print("Sumatoria del 0 al 100: ")
for j in range(1, 101):     # Creamos la variable j en el rango(1,101) para no coger ni el "0" y llegar a la iteración 100.
    sumatoria = j * (j + 1) // 2    # Construimos la variable sumatoria para realizar la operación en el código
    if j == 1:  # Desarrolamos esta primera sentencia alternativa para que cuando j= 1 se escriba correctamente la salida de texto
        print(f"{j} + ", end="")    # esta impresion, solo contiene el primer valor de la iteración, en este caso el 1
    elif j < 100: # Esta sentencia, engloba todos los valores menos el primero y el último
        print(f"{j} = {sumatoria} + ", end="")  # Para el print ingresamos el numero de iteración, mas la suma esta el numero dado acabando con un "+"
    else:
        print(f"{j} = {sumatoria}")

    # 4)  Escriure un programa que mostri la sumatòria de tots els múltiples de 3
    # trobats entre el 0 i el 100.
print("Mostrando sumatoria de los multiplos de 3 menores a 100")
suma = 0
for k in range(1, 100, 3):
    suma += k
    if k == 1:
        print(f"{k} +", end="")
    elif 1 < k < 99:
        print(f" {k} = {suma} +", end="")
    else:
        print(f" {k} = {suma}")
print()

#   5) Escriure un programa que mostri el ressò de tot allò que l'usuari
# introdueixi fins que l'usuari escrigui “sortir” que s'acabarà.
print("Ingresa lo que quieras, para salir, escribe salir")
y = ""
while y != "salir":
    y = input("$: ")
    print(y)
# 6) Escriviu un programa que demani un nombre enter més gran que zero i
# que escrigui els seus divisors.

print("Iniciando programa calculador de divisores")
entero = int(input("Introduce un número entero mayor a 0 o salir: "))
if entero <= 0:
    print("Número ingresado incorrecto, introduce un número correcto: ")
else:
    for q in range(1, entero + 1):
        if entero % q == 0:
                print(q)

#7)  Escriu un programa que mostri tots els enters positius senars menors
# que 100, excepte els que siguin divisibles per 7.

print("Iniciando programa para mostrar números enteros positivos menores de 100, excepto divisbles de 7")
n = 100

for v in range(1, n + 1):
    senars = 2 * v + 1
    if senars % 7 != 0 and senars < 100:
        print(senars)
