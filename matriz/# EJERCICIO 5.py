# EJERCICIO 5
U = int(input("Número de usuarios: "))
P = int(input("Número de películas: "))


ratings = []
for i in range(U):
    fila = []
    print(f"Usuario {i}:")
    for j in range(P):
        while True:
            try:
                r = int(input(f" Calificación para película {j} (1-5): "))
                if 1 <= r <= 5:
                    fila.append(r)
                    break
                else:
                    print("Debe ser un entero entre 1 y 5.")
            except ValueError:
                print("Ingresa un entero válido.")
        ratings.append(fila)


print("\nMatriz de calificaciones (U x P):")
for fila in ratings:
    print(fila)


# Promedio de una película (columna)
col = int(input(f"\nElige índice de película (0..{P-1}) para promedio: "))
if 0 <= col < P:
    suma = 0
    for i in range(U):
        suma += ratings[i][col]
        promedio_col = suma / U if U > 0 else 0
        print(f"Promedio de la película {col}: {promedio_col:.2f}")
else:
    print("Índice de película fuera de rango.")


# Vector de calificaciones de un usuario (fila)
row = int(input(f"\nElige índice de usuario (0..{U-1}) para ver su vector: "))
if 0 <= row < U:
    print(f"Vector del usuario {row}: {ratings[row]}")
else:
    print("Índice de usuario fuera de rango.")