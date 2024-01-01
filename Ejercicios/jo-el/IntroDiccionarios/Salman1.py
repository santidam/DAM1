casos = int(input())
for _ in range(casos):
    diccionario = {}
    lineas = int(input())
    for __ in range(lineas):
        if __ <= lineas-2:
            amigos = input().split(" ")
            amigo1 = amigos[0]
            mejorAmigo = amigos[1]
            if mejorAmigo in diccionario:
                diccionario[mejorAmigo] = amigo1
            else:
                diccionario[amigo1] = mejorAmigo
        else:
            nombre = input()
    print(diccionario[nombre])
