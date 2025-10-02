import numpy as np

#1. crear un conjunto de datos (matriz de 3x4)
# le segunda columna (indice 1) es la que se eliminará

datos = np.array ([
    [10, 20, 30, 40],
    [15, 20, 35, 45],
    [25, 20, 45, 55]
])

print("--- conjunto de datos original ---")
print(datos)

#2. Eliminar la columna de datos irrelevantes
#np.delete() se utiliza para eliminar elementos o filas/columnas
#axis=1 inidica que se debe de eliminar una columna
#el segundo argumento es el indice de la columna a eliminar (en eseta caso, 1)
datos_limpios = np.delete(datos, 2, axis=0)
datos_limpios = np.delete(datos, 3, axis=1)

print("\n--- conjunto de datos limpios ---")
print(datos_limpios)

#valores para axis
#axis=1 -> columnas
#axis=0 -> filas
#axis = None -> todo el array