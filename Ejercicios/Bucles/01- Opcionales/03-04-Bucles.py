# 3) Construye un triángulo isosceles con el número entero entregado por el usuario

altura = int(input("Introduce la altura del trángulo: "))

for i in range(altura):
    print((altura - i) * " ", (2 * i + 1) * "*")


 # 4) En el trángulo anterior construyelo de tal manera que en cada línea
# par aparezca una "o", centradas en líneas pares y cada 3 asteriscos

for i in range(altura):
    if i % 2 != 0:
        print((altura - i) * " ", "*" + "o" + "*" )
    print((altura - i) * " ", (2 * i + 1) * "*")

