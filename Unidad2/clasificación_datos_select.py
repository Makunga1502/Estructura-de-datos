# Lista de puntuaciones de relevancia de los productos
puntuaciones = [8, 3, 6, 1, 9, 4, 5, 2, 7, 9]

print("Puntuaciones originales:")
print(puntuaciones)

# Algoritmo de ordenamiento por selección (de menor a mayor)
n = len(puntuaciones)
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if puntuaciones[j] < puntuaciones[min_idx]:  
            min_idx = j

    
    puntuaciones[i], puntuaciones[min_idx] = puntuaciones[min_idx], puntuaciones[i]

print("\nPuntuaciones ordenadas de menor a mayor:")
print(puntuaciones)
