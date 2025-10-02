# EJERCICIO 7
N = 5
print("Llena el tablero 5x5 con 0 (vacío) o 1 (obstáculo):")
tablero = []
for i in range(N):
    fila = []
    for j in range(N):
        while True:
            try:
                c = int(input(f"Celda ({i},{j}) = "))
                if c in (0, 1):
                    fila.append(c)
                    break
                else:
                    print("Solo 0 o 1.")
            except ValueError:
                print("Ingresa 0 o 1.")
    tablero.append(fila)


print("\nTablero:")
for fila in tablero:
    print(" ".join(str(x) for x in fila))


# Conteo total de obstáculos
obstaculos_totales = 0
for i in range(N):
    for j in range(N):
        obstaculos_totales += tablero[i][j]
        print(f"\nObstáculos totales: {obstaculos_totales}")


# Conteo en fila específica
f = int(input(f"Fila para contar obstáculos (0..{N-1}): "))
if 0 <= f < N:
    obst_fila = sum(tablero[f])
    print(f"Obstáculos en la fila {f}: {obst_fila}")
else:
    print("Fila fuera de rango.")