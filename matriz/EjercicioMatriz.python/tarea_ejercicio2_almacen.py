# Inventario: [ID, cantidad, precio]
inventario = [
    [101, 50, 20.0],
    [102, 30, 15.5],
    [103, 20, 40.0]
]

# Imprimir inventario
print("ID | Cantidad | Precio")
for producto in inventario:
    print(producto)

# Calcular valor de un producto (ejemplo: producto 2)
i = 1
valor = inventario[i][1] * inventario[i][2]
print(f"\nValor total producto {inventario[i][0]}: {valor}")

# Vender 10 unidades
inventario[i][1] -= 10
print("Inventario actualizado:", inventario)
