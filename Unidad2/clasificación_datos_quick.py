def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)


puntuaciones = [0.2, -0.5, 1.0, -0.9, 0.4, 0.8]
ordenadas = quicksort(puntuaciones)
print("Puntuaciones ordenadas:", ordenadas)
