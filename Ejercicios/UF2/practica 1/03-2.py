import math

import matplotlib.pyplot as plt

# Construïm la llista amb els valors de les abscisses (eix x)

abscisses=[x/100 for x in range(700)]

# Construïm la llista amb els valors de les ordenades (eix y)

ordenades=[math.sin(x) for x in abscisses]

# Aconseguim un 'entorn virtual' (una figura i uns eixos) on dibuixar

dibuix,axes = plt.subplots()

# Dibuixa la gràfica sobre els axes obtinguts anteriorment

axes.plot(abscisses, ordenades)

# Mostra la gràfica a l'usuari

plt.show()