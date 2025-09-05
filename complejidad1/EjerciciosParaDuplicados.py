import time

def tiene_duplicado_linea(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

#pruebas con diferentes tamaños de arreglos
sizes = [100, 1000, 10000, 100000]

for n in sizes:
    arr = list(range(n)) # Arregglo sin duplicados para forzar el peorcaso

    star_line = time.time()
    tiene_duplicado_linea(arr)
    end_time = time.time()

    print(f"Busqueda de duplicados en un arreglo de {n} elementos: {end_time - star_line}")