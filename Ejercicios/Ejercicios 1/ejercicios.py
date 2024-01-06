# :Ejercicios.
# :1)
a = float(input("introduce un número: "))
b = float(input("introduce otro número: "))
print("el primero número que has introducido es", a, "el segundo número que has introducido es", b)
print("el resultado de la suma es:", a + b, "el resultado de la resta es:", a - b, "el resultado de la multiplicación es: ", a * b, "el resultado de la división es", a / b)
# :2) introducimos otra variable de cambio, a = b, b = a
print("la primera varibale a es", a, "la segunda variable b es", b)
print("Ahora efectuaremos una cambio de varibale, a será b, y b será a")
c = a
a = b
b = c
print("La variable a es", a, "la variable b es", b)
# :3) escribe un código que resuelva a + b / 2 * (a + b)
x = b / 2
y = a + b
print("ahora resolveremos a + b / 2 * (a + b) con la variable a: ", a, "y la variable b: ", b, " que has introducido anteriormente")
print("primero realizamos la primera division de b/2 que nos da", x, "despues multiplicamos este resultado por a + b que es: ", y, "y obtenemos", x * y)
print("para finalizar sumamos la variable a", a, "a b / 2 * (a + b) y obtenemos", a + x * y)
print(a + b / 2 * (a + b))

# :4) Demana un número a l’usuari. Mostra el seu número anterior i posterior

a1 = float(input("introduce otro número"))
print("el número que has introducido es ", a1)
print("se mostrara el número anterior y posterior de", a1)
b1 = a1-1
c1 = a1+1
print("número anterior: ", b1)
print("número posterior: ", c1)

# :5) Demana 4 notes a l’usuari entre 0 i 10. Calcula i mostra la seva mitjana

print("Introduce 4 notas para calcular la media de ellas")
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
n5 = n1 + n2 + n3 + n4
n6 = n5 / 4
print("la media de las 4 notas que has introducido es: ", n6)

# :6) Demana a l’usuari la base i alçada d’un rectangle i mostra el seu perímetre i l’àrea.

print("introduce los datos para calcular área y perimetro de un rectángulo")
e61 = float(input("introduce altura: "))
e62 = float(input("introduce base: "))
e63 = e61 * e62
e64 = (e61 * 2) + (e62 * 2)
print("el área del rectángulo es: ", e63)
print("el perímetro del rectángulo es: ", e64)

# 7) Demana una quantitat de minuts i mostra per pantalla a quantes hores i minuts correspon. Per exemple: 1000 minuts són 16 hores i 40 minuts.

e7 = float(input("introduce una cantidad de minutos: "))
e71 = e7 // 60   # :horas
e72 = e7 % 60    # :minutos
print("las horas y minutos son: ", e71, "h:", e72, "m")

# :8) Demana una hora a l’usuari entre 0 i 23. Demana que indiqui un minut,
# :entre 0 i 59. Per últim demana els segons, entre 0 i 59. Mostra l ’hora
# :introduïda i mostra posteriorment l’equivalent en segons.
# :exemple de sortida de l’exercici:

e8 = float(input("introduce un número entre 0 y 23 para horas: "))
if e8 <= 23 and e8 >= 0 :
    print("Horas OK")
elif e8 < 0 :
    print("Error, intruduce un número más alto: ")
else:
    print("Error, introduce un número bajo: ")
e81 = float(input("introduce un úmero entre 0 y 59 para minutos: "))
if e81 <= 59 and e81 >= 0 :
    print("Minutos OK")
elif e81 < 0 :
    print("Error, introduce un número mas alto: ")
else :
    print("Error, introduce un número mas bajo: ")
e82 = float(input("introuce un número entre 0 y 59 para segundos: "))
if e82 <= 59 and e82 >= 0 :
    print("Segundos OK")
elif e82 < 0 :
    print("Introduce un número mas alto: ")
else :
    print("Error, introduce un número mas bajo: ")

e83 = e8 * 3600
e84 = e81 * 60
e85 = e83 + e84 + e82

print("la cantidad de segundos es", e85)

# :9)Un gamer gasta el seu pressupost mensual amb la següent distribució:
# :15%menjar / sopar a domicili
#: 60%jocs nous
# :25%material otaku
# :emana el pressupost del mes i mostra quants diners gastarà en cada cosa

e9 = float(input("introduce tu presupuesto mensual: "))
e91 = e9 * 0.15  # :comida
e92 = e9 * 0.6   # :juegos
e93 = e9 * 0.2   # :material otaku
print("tu presupuesto para comida y cena a domicilio es: ", e91)
print("tu presupuesto para juegos nuevos es: ", e92)
print("tu presupuesto para material otaku es: ", e93)

# :10)  Un usuari disposa de diners per comprar-se una peça de roba que està)
# :te rebaixes amb un 25% de descompte. Demana a l’usuari el diners que
# :té i el preu de la peça. Mostra el preu que li quedarà amb el descompte i
# : quants diners li quedaran després de fer la compra. (Observacions:
# :evidentment, el preu i els diners són números decimals).

e10 = float(input("Hola,introduce la cantidad de dinero que tienes: "))
e101 = float(input("Ahora introduce el precio de lo que quieres comprar: "))
e102 = e101 * 0.75
e103 = e10 - e102
print("Lo que deseas comprar tiene un descuento de un 25%, su precio actual es: ", e102)
print("Despues de comprar el objeto te quedarán: ", e103)
