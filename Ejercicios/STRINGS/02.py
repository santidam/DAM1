x = input("Introduce una cadena y un caracter: ")
nombres = x.split(" ")
cadena = nombres[0]
caracter = nombres[1]
if len(caracter) > 1:
    print("Error, has introducido más de un carácter")
else:
    print(f"En la cadena {cadena}, el caracter {caracter}, se encuentra {cadena.count(caracter)} veces")
