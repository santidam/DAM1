casos = int(input())
for _ in range(casos):
    diccionario = {}
    casos2 = int(input())
    for __ in range(casos2-1):
        paisCapital = input().split("-")
        pais = paisCapital[0]
        capital = paisCapital[1]
        diccionario[pais] = capital
    usuario = input()
    if usuario in diccionario:
        print(diccionario[usuario])
    else:
        print("NO HO SE")
