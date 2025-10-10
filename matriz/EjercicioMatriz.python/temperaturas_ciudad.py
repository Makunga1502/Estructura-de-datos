temperaturas = [
    [20.0, 27.4, 31.3],
    [21.5, 28.0, 32.1],
    [19.8, 26.5, 30.0],
]

print("temperaturas de la ciudad(en °C):")
for fila in temperaturas:
    print(fila)

print("\nTemperaturas de la semana:", temperaturas[1][1], "°C")

nueva_temp = float(input("Ingrese la nueva temperatura para el día central: "))
temperaturas[1][1] = nueva_temp 

print("\nTemperaturas actualizadas:")
for fila in temperaturas:
    print(fila)