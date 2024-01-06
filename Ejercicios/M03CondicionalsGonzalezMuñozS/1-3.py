
#1. [0,5 punts] Escriu el codi necessari per demanar dos números enters a
#l’usuari entre 1 i 100. Guarda’ls a les variables num1 i num2. Mostra'ls per
#pantalla. Indica si num1 i num2 estan dins del rang demanat (entre 1 i
#100).

num1 = int(input("Introduce un número entero entre 1 y 100: "))    # en este punto, creamos dos variables de integers que son ingresadas por el usuario,
num2 = int(input("Introduce otro número entero entre 1 y 100: "))  # para ello usamos int(input()), las variables serán num1 y num2
print("El primer número introducido es: ", num1)    # Imprimimos en pantalla las variables introducidas por el usuario, num1 y num2
print("El segundo número introducido es: ", num2)
if num1 >= 1 and num1 <= 100:    # Creamos la primera condicional con "if" para determinar que "num1" se encuentra entre 1 y 100, para ello usamos
    print("El primer número introducido está en el rango")  # comparadores del tipo x >= y y viceversa, si la variable es correcta imprimimos en pantalla que está en el rango
else:   # Cerramos la condicional de arriba con "else" para que cualquier número entregado en la varible num1 por el usuario que no esté dentro del rango que hemos
    print("El primer número introducido no está en el rango") # creado en el "if" anterior imprima en pantalla el mensaje "no está en el rango"
if num2 >= 1 and num2 <= 100: # Al igual que con la varable anterior, ene ste "if" establecemos el mismo rango numerico para la variable num2
    print("El segundo número está en el rango") # Si la variable está en el rango, lo confirmamos
else:  # Al igual que antes, si la variable no está en el rango imprimimos el mensaje de invalidación
    print("El segundo número introducido no está en el rango")

# 2. [0,5 punts] Escriu el codi necessari que indiqui si la variable num2 és
# parell.

if num2 % 2 == 0:  # En este punto, para determinar si la variable num2 es par, usamos el operador " x % 2 == 0", con el que obtenemos el resto del dividendo entre el divisdor 2
    print("La segunda variable ", num2, "introducida es par")  # si el resto de esta operación es 0, el número será par. Por lo tanto si se cuumple la condional, imprimimos " es par"

# 3. [0,5 punts] Escriu el codi necessari que indiqui si num1 i num2 són
# imparells.

if num1 % 2 != 0: # Para determinar que las variables introducidas son impares, al igual que el ejercicio anterior, realizamos la operación "x % 2" != 0
    print("El primer número introducido: ", num1, "es impar")   # en la cual, para cualquier resto diferente (!=) a 0, será impar, despues imprimimos
if num2 % 2 != 0:   # Realizamos el mismo procedimiento anterior para la variable num2
    print("El segundo número introducido: ", num2, "es impar")  # si la variable cumple los requisitos de la comparación imprimimos, es impar.