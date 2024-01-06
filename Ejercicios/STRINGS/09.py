x = input("Introduce una frase: ")
#1)
vocales = 0
for i in x:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i, end="")
        vocales += 1

print(f"\n"
      f"La frase tiene {vocales} vocales")
#2)
print(x.count("a") + x.count("e") + x.count("i") + x.count("o") + x.count("u"))
#3)
vocales = "aeiou"
contador = 0
for i in vocales:
    contador += x.count(i)
print(f"Vocales: {contador}")