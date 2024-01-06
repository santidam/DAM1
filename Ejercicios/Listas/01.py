#Listas : coleccion da datos, se neceista inicializar, dandole un valor inicial, es sinonima de array
vacia = [] #lista vacía
nums = [1,2,8,6,4,3]
lista = ["Pedro", 53,6, True]
datos = [1,[5,8,3],6]   # Si hay una matriz dentro de otra, se puede ejecutar como mátriz
tablero = [[1,0,0],[0,2,0],[0,1,0]] # matriz, lista en dos dimensiones"
#print(lista)
#print(nums[2])
# print(nums[88]) # da error porque la posicion debe estar entyre 0 y len(nums)-1 que es longitud -1
#print(len(nums))
#for n in lista:
 #   print(n)
for i in range(len(lista)):
    print(nums[i])

vacia.append(5) # añade datos a la lista, solo 1
vacia.extend([3,4,8]) # añade varios elementos la final de la lista
vacia.insert(0,8) # inserta el dato en la posición 0, reeorganizando los datos de la lista
vacia.sort() #ordena la lista en orden creciente, de mayor a menor
#vacia.sort(reverse:True) #ordena la lista en orden creciente, de mayor a menor
print()
print(nums[-1]) #pritnea ultimo valor
print()
print(nums[1:4]) # imrpime los numeros dentro del rango
if 3 in nums:
    print(nums)
if "nom" not in lista:
    print(lista)
nombre = input()
nombre.lower() # transforma el dato en minusculas
nombre.upper() # transforma el dato en mayusculas
nombre.capitalize() # Primera letra en mayuscula y el resto en minuscula
del