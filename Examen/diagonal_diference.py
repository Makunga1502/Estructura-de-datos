matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def diagonal_difference(matrix):
    n = len(matrix)
    primera_diagonal = 0
    segunda_diagonal = 0
    
    for i in range(n):
        primera_suma_diagonal = matrix [i][i]
        segunda_suma_diagonal = matrix[i][n - 1 - i]


        primera_diagonal += primera_suma_diagonal
        segunda_diagonal += segunda_suma_diagonal

    print("\nla primera suma diagonal nos da como resultado:" , primera_diagonal)
    print("la segunda suma diagonal nos da como resultado:" , segunda_diagonal)

    return(primera_diagonal - segunda_diagonal)

resultado = diagonal_difference(matriz)
print("\nla resta entre las diagonales nos da como resultado:" , resultado)

