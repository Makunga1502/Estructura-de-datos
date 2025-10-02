 # Entrenamiento de una red neuronal

entrada = [1, 2]

# Matriz Pesos 3 x 2
#
pesos =[
    [4,1,5,6],
    [4,1,5,6]
]

salida = [0,0,0,0]

for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]


print(salida)