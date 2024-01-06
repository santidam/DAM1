meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo,", "Junio", "julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
numero = int(input("Introduce el numero del mes: "))
while numero <=0:
    print("Introduce un número valido entre 1 y 12")
print(f"El mes seleccionado es: {meses[numero - 1]}\n"
      f"Tiene: {dias[numero - 1]}")