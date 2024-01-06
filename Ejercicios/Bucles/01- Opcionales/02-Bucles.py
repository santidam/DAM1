# 2) Escribe un programa que pida al usuario un número entero y muestre un tríángulo rectángulo inverso:
altura = int(input("Ingresa la altura del triángulo: "))

for i in range(1, altura + 1):
    print((altura - i) * " " + i * "*")