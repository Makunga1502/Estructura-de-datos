import numpy as np

# Creamos una matriz de ejemplo (conjunto de datos)
# Cada fila es un registro y cada columna una característica
datos = np.array([
    [1, 25, 180, 0],
    [2, 30, 175, 1],
    [3, 22, 169, 0],
    [4, 28, 182, 1]
])

print("Matriz original:")
print(datos)

# Supongamos que la última columna es irrelevante (por ejemplo, con errores)
datos_limpios = np.delete(datos, 3, axis=1)

print("\nMatriz después de limpiar (sin la última columna):")
print(datos_limpios)
