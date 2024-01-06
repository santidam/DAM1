#Exercici 1
#Escriure un programa que pregunti el nom complet de l'usuari a la consola
#i després mostri per pantalla el nom complet de l'usuari tres vegades, una
#amb totes les lletres minúscules, una altra amb totes les lletres majúscules
#i una altra només amb la primera lletra del nom i dels cognoms en
#majúscula. L'usuari pot introduir el nom combinant majúscules i minúscules
#com vulgui.
x = input("Introduce tu nombre completo: ")
x2 = x + " "
for i in range(3):
      print(x)
print(f"{x2 * 3}\n"
      f"{x.lower()}\n"
      f"{x.upper()}\n"
      f"{x.capitalize()}\n"
      f"{x.title()}")
