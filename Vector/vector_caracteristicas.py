caracteristicas_flor = [3.5, 1.4, 0.2]

suma_total = sum(caracteristicas_flor)

vector_normalizado = [x / suma_total for x in caracteristicas_flor]

print("vector original", caracteristicas_flor)
print("suma total", suma_total)
print("vector normalizado", vector_normalizado
      )