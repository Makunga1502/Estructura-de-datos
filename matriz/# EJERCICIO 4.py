# EJERCICIO 4
precisiones = []
print("Ingresa precisiones por época. Escribe 'fin' para terminar.")
while True:
    dato = input("Precisión (0-1 o 0-100): ")
    if dato.strip().lower() == 'fin':
        break
    try:
        val = float(dato)
        # Normaliza si parece porcentaje (ej. 87 -> 0.87)
        if val > 1:
            val = val / 100.0
        if 0 <= val <= 1:
            precisiones.append(val)
        else:
            print("Ingresa un valor entre 0 y 1, o porcentaje 0-100.")
    except ValueError:
        print("Valor inválido.")


if precisiones:
    precision_final = precisiones[-1]
    precision_max = max(precisiones)
    print(f"Precisión final: {precision_final:.4f}")
    print(f"Precisión más alta: {precision_max:.4f}")
else:
    print("No se ingresaron precisiones.")