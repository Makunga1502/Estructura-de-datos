# Crear matriz 3x2 para representar las conexiones entre neuronas
pesos = [
    [1,2],
    [3,4],
    [5,6]
]

# Iniciañizar un vector de entrada y realizar producto punto

entrada = [1, 2, 3]
salida = [0, 0]

for j in range(2):
    for i in range(3):
        salida[j] += entrada[i] * pesos[i][j]

print("Vector de entrada:", entrada)
print("Matriz de pesos:", pesos)
print("Vector de salida:", salida)