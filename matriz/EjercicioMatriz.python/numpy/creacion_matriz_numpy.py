import numpy as np

#creación de una matriz 3x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#imprimir matriz original
for fila in matriz_A:
    for elemento in fila:
        print(elemento, end= " ")
    print()

print("***************")

#crear una matriz de ceros
matriz_B = np.zeros((2, 3))

for fila in matriz_B:
    for elemento in fila:
        print(elemento, end= " ")
    print("")

