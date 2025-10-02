# Matriz de pesos (3x2)
pesos = [
    [0.2, 0.8],
    [0.5, 0.1],
    [0.9, 0.4]
]

# Vector de entrada (3x1)
entrada = [1.0, 0.5, 0.2]

# Calcular producto punto
salida = [0, 0]
for j in range(2):  # columnas de la matriz
    for i in range(3):  # filas de la matriz
        salida[j] += entrada[i] * pesos[i][j]

print("Entrada:", entrada)
print("Pesos:", pesos)
print("Salida:", salida)
