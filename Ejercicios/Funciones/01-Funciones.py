#Es necesario definir funcion para utilizarla. Se definen parametros dentro de "()" de la funcion
# Ejemplo:
def hello(name="Patata", age=25): # Definimos procedimiento con valores predeterminados en caso de que no se definan dichos valores
    if age > 50:
        print("You are young! and funny!")
    else:

        print("You are a baby", name)

hello(5)

def suma(num1, num2):       #Definimos funcion que suma elementos.
                            # Tambien se puede llamar: "Procedimiento o procedure": trozo de codigo que no devuelve nada, "funcion": devuelve un valor, "metodo": procedimiento o funcion que esta dentro de una clase
    resultado = num1 + num2
    return resultado # Return: devuelve un valor en una variable, debes crearla, en este caso "x"

x = suma(8,2)
print(x)

def cambiaNnum(a):
    a = a + 1
a = 2
cambiaNnum(a)
print(a)
def cambiarLista(nums):
    nums.append(8)
lista = [1,2,3]
cambiarLista(lista)
print(lista)

#Las variables complejas si se modifican en la función aún sin tener "return"
#Las variables simples no se ven módificadas al usar la función