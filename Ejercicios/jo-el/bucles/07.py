k = int(input())
while k != 0:
    numero = int(input())
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(factorial)
    k -= 1
