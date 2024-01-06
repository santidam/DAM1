# Escriu un programa que ens permeti desar els noms dels alumnes d'una
# classe i les notes que han obtingut. Cada alumne pot tindre diferent
# quantitat de notes. Guarda la informació en un diccionari la clau del qual
# seran els noms dels alumnes i els valors seran llistes amb les notes de cada
# alumne. No pot haver dos alumnes amb el mateix nom, evidentment.
# El programa demanarà el nombre d'alumnes que introduirem, demanarà el
# seu nom i anirà demanant les notes fins que introduïm un número negatiu.
# Al final, el programa ens mostrarà la llista d'alumnes i la nota mitjana
# obtinguda per cadascun.

diccionario = {}
# Me ha faltado preguntarle al ususario la cantidad de de alumnos que introducirá
salir = True
while salir == True:
    nombre = input("introduce el nombre del alumno o salir para salir: ").lower()
    if nombre == "salir":
        salir = False
    elif nombre in diccionario:
        print("Error, el alumno ya está en la lista")
    else:
        listaNotas = []
        nota = 0
        suma = 0
        while nota >= 0:
            nota = int(input("Introduce las notas del alumno, negativo para salir: "))
            if nota >= 0:
                suma += nota
                listaNotas.append(nota)
        if suma == 0:
            diccionario[nombre] = {"notas": listaNotas, "Media": 0}
        else:
            diccionario[nombre] = {"notas":listaNotas, "Media" : suma/len(listaNotas)}
for i in diccionario:
    print(i.capitalize(), diccionario[i])

# diccionario.items() --> para iterar sin comillas
