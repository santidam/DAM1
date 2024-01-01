k = int(input())
if k <= 0:
    print("ELS NOMBRES NATURALS COMENCEN EN 1")
else:
    for i in range(k):
        numero = int(input())
        suma = 0
        mult = 1
        if numero <= 0:
            print("ELS NOMBRES NATURALS COMENCEN EN 1")
        else:
            for j in range(1, numero + 1):
                suma += j
                mult *= j
            print("SUMA:", suma, "PRODUCTE:", mult)
