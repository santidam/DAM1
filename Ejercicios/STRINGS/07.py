x = input("Introcue un numero entero positivo: ")
while x.isnumeric() == False or int(x) < 0:
    x = input("Introduce un número entero positivo: ")
print(x)


