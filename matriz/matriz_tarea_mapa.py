import random

# Crear mapa 8x8 aleatorio con valores 0, 1, 2
mapa = [[random.randint(0, 2) for _ in range(8)] for _ in range(8)]

# Contadores
precaucion = 0
alto_riesgo = 0

for fila in mapa:
    for valor in fila:
        if valor == 1:
            precaucion += 1
        elif valor == 2:
            alto_riesgo += 1

# Actualizar el mapa: convertir 2 en 1
for i in range(8):
    for j in range(8):
        if mapa[i][j] == 2:
            mapa[i][j] = 1

print("Mapa actualizado:")
for fila in mapa:
    print(fila)

print("Áreas de precaución:", precaucion)
print("Áreas de alto riesgo:", alto_riesgo)

