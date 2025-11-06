# Lista de alertas 
alertas = [0.45, 0.92, 0.12, 0.78, 0.33, 0.67, 0.89, 0.23, 0.56, 0.10]

print("Alertas originales:")
print(alertas)

# Algoritmo de ordeanmiento por selección
n = len(alertas)
for i in range(n - 1):
    max_idx = i
    for j in range(i + 1, n):
        if alertas[j] > alertas[max_idx]: 
            max_idx = j

    alertas[i], alertas[max_idx] = alertas[max_idx], alertas[i]

print("Alertas ordenadas de mayor a menor:")
print(alertas)