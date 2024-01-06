# 8. [2 punts] Els tres costats a, b i c d'un triangle han de satisfer la
# desigualtat triangular: cadascun dels costats no pot ser més llarg que la
# suma dels altres dos.
# Escriu un programa que demani els tres costats d'un triangle i indiqui:
# ● si el triangle és invàlid
# ● si no ho és, quin tipus de triangle és (equilàter, isòsceles, escalè).

print("Iniciando programa de validación de triángulos") #
a = float(input("Introduce el valor del primer lado: "))
b = float(input("Introduce el valor del segundo lado: "))
c = float(input("Introduce el valor del tercer lado: "))
if a + b > c and a + c > b and b + c > a:
    print("El triangulo introducido es valido ")
    if a == b and a == c:
        print("El triangulo introducido es equilatero")
    elif a == b and a != c or b == c and b != a:
        print("El triangulo introducido es isosceles")
    elif a != b or a != c or b != c:
        print("El triangulo introducido es escaleno")
else:
    print("El triangulo introducido es invalido")

