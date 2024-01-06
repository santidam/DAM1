

sumatoria = 0
for numero in range(101):
    sumatoria += numero
    if numero < 100:
        print(f"el {numero} + ", end="")
    else:
        print(f"{numero} = {sumatoria}")
print("la sumatoria es: ", sumatoria)

