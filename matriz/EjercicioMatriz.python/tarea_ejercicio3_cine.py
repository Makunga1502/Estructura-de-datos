# Inicializar mapa de asientos
cine = [[0]*5 for _ in range(4)]

# Mostrar mapa inicial
print("Mapa de asientos:")
for fila in cine:
    print(fila)

# Marcar un asiento ocupado
fila = int(input("Ingresa la fila (0-3): "))
col = int(input("Ingresa el asiento (0-4): "))
cine[fila][col] = 1

# Mostrar mapa actualizado
print("\nMapa actualizado:")
for fila in cine:
    print(fila)

# Contar libres
libres = sum(fila.count(0) for fila in cine)
print(f"Asientos libres: {libres}")
