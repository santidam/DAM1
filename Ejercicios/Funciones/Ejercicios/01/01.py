#1. Funció EsMultiple. Rep dos números i indica si el primer és múltiple del
#segon. Paràmetres d’entrada: dos números. Valor de sortida: múltiple: Valor
#lògic Verdader si el primer és múltiple del segon, Fals en cas contrari.

def EsMultiple(num1, num2):
    if num2 % num1 == 0:
        multiple = True
        return multiple
    else:
        multiple = False
        return multiple
x = EsMultiple(2,2)
print(x)

#2. Funció CalcularTemperaturaMitja: Rep dos números reals que representen
#dues temperatures i retorna la temperatura mitja. Paràmetres d’entrada: dues
#temperatures (float) Valor de sortida: La temperatura mitja (float).

def CalcularTemperaturaMitja(num1, num2):
    temperaturas = []
    temperaturas.append(num1)
    temperaturas.append(num2)
    temperaturaMedia = (temperaturas[0] + temperaturas[1]) / len(temperaturas)
    return temperaturaMedia
x = CalcularTemperaturaMitja(10.5,5)
print(x)

#3. Funció CalcularFactorial: Rep un número si el número=1 retorna que el
#factorial és 1, sinó acumula el producte del número amb el càlcul del factorial
#del número-1. Paràmetres d’entrada: número. Valor de sortida: Factorial del
#número

def CalcularFactorial(num1):
    if num1 == 1 or num1 == 0:
        factorial = 1
        return factorial
    elif num1 > 1:
        factorial = 1
        for i in range(1, num1):
            factorial *= i
        return factorial
    return 0
# una funcion recursiva se llama a sí misma dentro de la misma función

x = CalcularFactorial(3)
print(x)

#4. Funció Convertir_A_Segons: Rep una quantitat d’hores, minuts i segons i
#calcula a quants segons correspon Paràmetres d’entrada: hora, minuts i
#segons. Valors de sortida: Segons totals

def Convertir_A_Segons(num1, num2,num3):
    segundos = num1 * 3600 + num2 * 60 + num3
    return segundos
x = Convertir_A_Segons(1,1,5)
print(x)

# 5. Funció EsBisiesto: Rep un any i retorna si és o no és bisiesto Paràmetres
# d’entrada: any. Valor de sortida: Valor lògic indicant si és bisiesto (Verdader) o
# no (Fals)

def EsBisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        bisiesto = True
        return bisiesto
    else:
        bisiesto = False
        return bisiesto
x = EsBisiesto(2022)
print(f"Año bisiseto = {x}")

#6. Realitza una funció anomenada parells(lista) que prengui una llista de
# nombres enters i que retorni una llista amb els nombres parells de la llista
def parells(lista):
    lista2 = []
    for i in lista:
        if i % 2 == 0:
            lista2.append(i)
    return lista2
x = parells([-12, 84, 13, 20, -33,101,9])
print(x)

#7. Realitza una funció anomenada validar(string) que indiqui si el text que se li
#ha adjuntat és una adreça de correu electrònic o no. Es considerarà que una
#adreça és vàlida si inclou en el seu interior el símbol “@”, tè contingut a la dreta
#i esquerra de “@” i al menys té un punt a la part dreta.

def validar(string):
    if "@" in string:
        partes = string.split("@")
        parte1 = partes[0]
        parte2 = partes[1]
        if len(partes) == 2:
            if len(parte1) > 0 and len(parte2) > 1 and "." in parte2:
                validacion = True
            else:
                validacion = False
            return validacion
        else :
            validacion = False
            return validacion
    else:
        validacion = False
        return validacion
x = validar("a@.p")
print(x)

#8 Demana a l’usuari que introdueixi un nombre enter i positiu i, mitjançant una
#funció, determina si el nombre és primer o no ho és, de manera que la funció
#retorni un valor booleà que ho indiqui. Has de “traduir” el resultat de la funció a
#un missatge que pugui entendre l’usuari.

def numeroPrimo(num1):
    primo = True
    x = ""
    for i in range(2, num1):
        if num1 % i == 0:
            primo = False
    if primo == True:
        x = "El numero introducido es primo"
    elif primo == False:
        x = "El numero introducido no es primo"
    return x


usuario = int(input("Introduce un número entero positivo: "))

x = numeroPrimo(usuario)
print(x)


# 9. Escriure una funció que, al donar-li un número de NIF ens digui si és vàlid o
# no. Un NIF serà vàlid si té 8 dígits i una lletra en majúscula. També heu de
# verificar si la lletra és correcta. La funció ens retornarà True o False.

def validarDni(num1):
    valido = True
    numeros = ["1","2","3","4","5","6","7","8","9"]
    letras = num1.split()
    if len(letras) == 9 and letras[-1].isalpha() == True and letras[-1].isupper == True:
        for i in range(len(letras)-1):
            if i in numeros and valido == True:
                valido = True
            else:
                valido = False
    else:
        valido = False
    return valido
usuario = input("Introduce un dni para validarlo: ")
x = validarDni(usuario)
print(x)

#10 





