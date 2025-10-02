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
    print("")

#acceder a un elemento (fila 1, columna 2)
elemento = matriz_A[1, 2]

print(elemento)

#modificar un elemento
matriz_A[0, 0] = 99

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end= " ")
    print("")