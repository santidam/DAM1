k = 0
deu = 0
total = 0
while k != -1:
    k = int(input())
    if k >= 0 and k <= 10:
        total += 1
    if k == 10:
        deu += 1
print("TOTAL NOTES:", total, "NOTES10:", deu)
