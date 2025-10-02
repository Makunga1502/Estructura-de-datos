# Vector de características: [longitud sépalo, longitud pétalo, anchura pétalo]
caracteristicas = [3.5, 1.4, 0.2]

# Calcular suma total
suma = sum(caracteristicas)

# Normalizar el vector
normalizado = [x / suma for x in caracteristicas]

print("Vector original:", caracteristicas)
print("Suma:", suma)
print("Vector normalizado:", normalizado)
