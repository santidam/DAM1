k = 1
car = 1
x = "NO"
y = 0
datos = ""
while k != 0 and car != 0:
    car = int(input())
    while datos != 0:
        k = input()
        if k != 0:
            datos = k.split(" ")
            n1 = int(datos[0])
            n2 = int(datos[1])
            if car * 1.5 >= n1 - n2:
                x = "SI"
                y += 1
    if y >= 1:
        print(x, y)
    else:
        print(y)
