# Matriz de recomendación de peliculas

matriz = [
 
    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	4],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	3],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	3],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	2],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	1],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	1],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	2],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	3],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	2],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]
 
 #imprimir la matriz de calificaciones

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c], end="")
    print()

#promedio de una pelicula

suma = 0
pelicula = 12

for f in range(len(matriz)):
    suma += int(matriz[f][pelicula])

print("La suma de calificaciones de la pelicula 1: ", suma)
promedio = suma / len(matriz)
print("El promedio de calificaiones de la pelicula 1 es: ", promedio)

calificacionesUsuario = matriz[0]
print("Las calificiaones usuario [0]: ", calificacionesUsuario)