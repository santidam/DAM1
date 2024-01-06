#Contador de notas
k = 10
total = 0
mitjana = 0
excelents = 0
notables = 0
be = 0
sufi = 0
insufi = 0
defi = 0
while k != -1:
    k = int(input())
    if k  >= 0 and k <= 10:
        total += 1
        mitjana += k
        mitjana2 = mitjana / total
        if k >= 9:
            excelents += 1
        elif k >= 7 and k <= 8:
            notables += 1
        elif k == 6:
            be += 1
        elif k == 5:
            sufi += 1
        elif k < 5 and k > 3:
            insufi += 1
        elif k >= 0 and k <= 3:
            defi += 1
print("NOTES:", total ,"MITJANA:", mitjana2, "E:", excelents ,"N:", notables ,"B:", be ,"S:", sufi, "I:", insufi ,"MD:", defi)


