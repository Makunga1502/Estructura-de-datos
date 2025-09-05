# Sistema de Recomendación de Películas con Matrices

# Matriz de calificaciones (usuarios x películas)
# Filas = usuarios, Columnas = películas
calificaciones = [
    [5, 3, 4, 4],
    [3, 1, 2, 3],
    [4, 3, 4, 5],
    [3, 3, 1, 5],
    [1, 5, 5, 2]
]

# Imprimir la matriz
print("Matriz de calificaciones (usuarios x películas):")
for fila in calificaciones:
    print(fila)

# Calcular el promedio de una película específica
pelicula = 2  # índice de la película (0 = primera, 1 = segunda, etc.)
suma = 0
for usuario in range(len(calificaciones)):
    suma += calificaciones[usuario][pelicula]
promedio = suma / len(calificaciones)
print(f"\nPromedio de la película {pelicula+1}: {promedio:.2f}")

# Mostrar vector de calificaciones de un usuario específico
usuario = 3  # índice del usuario
print(f"\nCalificaciones del usuario {usuario+1}: {calificaciones[usuario]}")