cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")
if cadena1.find(cadena2) == -1:
    print("La subcadena no se encuentra en la cadena")
else:
    print(f"En la cadena {cadena1}, la subcadena {cadena2} se encuentra: {cadena1.count(cadena2)} veces")