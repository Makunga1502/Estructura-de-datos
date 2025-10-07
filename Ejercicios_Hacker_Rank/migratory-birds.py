def MigratoryBirds(arr):
    freq = [0] * 6  # Inicializa una lista para contar la frecuencia de cada tipo de pájaro (1-5)
    for x in arr:
        freq[x] += 1  # Incrementa la frecuencia del tipo de pájaro correspondiente
    
    best_id = 1
    best_count = freq[1]
    for i in range(2, 6):
        #si encontramos un tipo de pajaro con mayor frecuencia o igual pero con id menor
        if freq[i] > best_count or (freq[i] == best_count and i < best_id):
            best_id = i
            best_count = freq[i]
    return best_id

print(MigratoryBirds([1, 4, 4, 4, 5, 3]))  
