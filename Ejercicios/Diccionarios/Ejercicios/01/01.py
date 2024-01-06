#Escriu un programa que pregunti a l'usuari el nom, l'edat, l'adreça i el
#telèfon i guardi la informació en un diccionari. Després ha de mostrar per
#pantalla el missatge “<nom> té <edat> anys, viu a <adreça> i el seu
#número de telèfon és <telèfon>”, amb les dades que ha introduït
#l’usuari.

diccionario = {}
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = int(input("Introduce tu teléfono: "))
diccionario[nombre] = {"Nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print(diccionario[nombre]["Nombre"], "té", diccionario[nombre]["edad"], "anys, viu a", diccionario[nombre]["direccion"], "i el seu número de telèfon és", diccionario[nombre]["telefono"])
