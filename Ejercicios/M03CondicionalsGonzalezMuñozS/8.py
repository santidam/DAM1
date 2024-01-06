# 8. [2 punts] Els tres costats a, b i c d'un triangle han de satisfer la
# desigualtat triangular: cadascun dels costats no pot ser més llarg que la
# suma dels altres dos.
# Escriu un programa que demani els tres costats d'un triangle i indiqui:
# ● si el triangle és invàlid
# ● si no ho és, quin tipus de triangle és (equilàter, isòsceles, escalè).

print("Iniciando programa de validación de triángulos") # Creamos un print al iniciar el programa, para dar información relativa a este
a = float(input("Introduce el valor del primer lado: "))    # Construimos las primeras variables, estas determinarán el valor de cada lado
b = float(input("Introduce el valor del segundo lado: "))   # del triángulo construido, para ello anteponemos float, para que los datos
c = float(input("Introduce el valor del tercer lado: "))    # ingresados por el usuario sean guardados como valores con parte decimal
if a + b > c and a + c > b and b + c > a: # Introducimos la primera sentencia alternativa, escribimos las tres comparaciones condicionales, acompañadas con los operadores logicos "and", buscando así que cada comparación sea true
    print("El triangulo introducido es valido ")    # Si se cumplen las condiciones, validamos la información ingresada por el usuario
    if a == b and a == c: # Anidamos la siguiente sentencia condicional en la cual determinaremos mediante igualdades, que todos los lados son inguales.
        print("El triangulo introducido es equilatero") # Si todos los lado sosn iguales, imprimimos el tipo de triángulo, en este caso equilatero
    elif a == b and a != c or b == c and b != a:    # En esta sentencia introducimos dos argumentos principales separados por el comparador lógico "or", si se cumple el primer argumento o el segundo, la sentencia será true.
        print("El triangulo introducido es isosceles") # En caso de que se cumplan, significará que estamos ante un triangulo isosceles, tras lo cual imprimimos dicha información.
    elif a != b and a != c and b != c:    # En esta última sentencia alternativa anidada al if principal, determinaremos mediante el operador de comparacion != que en caso de que todas las variables ingresadas sean diferentes, nos responderá un true.
            print("El triangulo introducido es escaleno")   # Si la sentencia anterior es true, sabremos que estamos ante un triángulo escaleno, por lo tanto imprimieremos en pantalla la información para el usuario.
else:   # Este else esta ligado a la primera sentencia alternativa construida, que determinará que en caso de que no se cumplan las condiciones de la desigualdad triangular, entonces el triangulo será invalido, y el programa terminará.
    print("El triangulo introducido es invalido")   # Imprimiremos en pantalla la información relativa a la invalidación del triángulo y el programa se cerrará


