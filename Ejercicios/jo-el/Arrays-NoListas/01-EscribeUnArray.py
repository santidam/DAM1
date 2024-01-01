k = int(input())
n = input()
j = int(input())
array = []
for i in range(k):
    numeros = n.split(" ")
    array.append(numeros[i])
for elemento in array:
    print(elemento, end=" ")
print()
print(array[j])
