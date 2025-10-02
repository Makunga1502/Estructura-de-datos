#limpieza de datos con numpy
import numpy as np

#simular una matriz de datos de 12 * 5
np.random.seed(42)
datos = np.random.rand(5, 5) * 100

#simular datos erroneos
datos[2, 3] = -99 #valor negativo
datos[2, 3] = 1000 #valor fuera de rango

print("Datos originales")
print(datos)

indices_erroneos = [0,2]

datos_limpios = np.delete(datos, indices_erroneos, axis=0)
print("\nDatos limpios:")
print(datos_limpios)