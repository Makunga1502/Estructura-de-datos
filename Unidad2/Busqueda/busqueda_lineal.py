def busqueda_secuecial(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    datos = [4, 2, 3, 5, 1]
    objetivo = 5

    indice = busqueda_secuecial(datos, objetivo)
    if indice != -1:
        print(f"Elemento {objetivo} encontrado en el índice: {indice}")
    else:
        print(f"Elemento {objetivo} no encontrado en la lista.")



