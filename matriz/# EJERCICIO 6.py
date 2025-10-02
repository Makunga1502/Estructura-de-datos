# EJERCICIO 6
nombres_dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
ventas = []
for i, d in enumerate(nombres_dias):
    while True:
        try:
            v = float(input(f"Ventas de {d}: "))
            ventas.append(v)
            break
        except ValueError:
            print("Ingresa un número.")


total = sum(ventas)
maximo = max(ventas)
minimo = min(ventas)
idx_max = ventas.index(maximo)
idx_min = ventas.index(minimo)


print(f"\nTotal semanal: {total:.2f}")
print(f"Día con más ventas: {nombres_dias[idx_max]} ({maximo:.2f})")
print(f"Día con menos ventas: {nombres_dias[idx_min]} ({minimo:.2f})")