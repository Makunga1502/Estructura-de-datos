luz= [
    [120, 150, 130, 160],
    [200, 180, 190, 170],
    [140, 160, 150, 180],
    [130, 140, 120, 110]
]

print("Intensidades de luz:")
for fila in luz:
    print(fila)

fila = int(input("Ingrese el número de fila (0-3) de la intensidad que desea modificar: "))
columna = int(input("Ingrese el número de columna (0-3) de la intensidad que desea modificar: "))
print(f"Intensidad actual en la posición ({fila}, {columna}): {luz[fila][columna]}") 

nueva_intensidad = float(input("Ingrese la nueva intensidad de luz: "))
luz[fila][columna] = nueva_intensidad

print("\nIntensidades de luz actualizadas:")
for fila_matriz in luz:
    print(fila_matriz)

suma = sum(sum(fila_matriz) for fila_matriz in luz)
total_elementos = len(luz) * len(luz[0])
promedio = suma / total_elementos