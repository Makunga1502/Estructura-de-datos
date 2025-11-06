correos = [45, 12, 78, 34, 23, 89, 56, 9, 67, 30]  


for i in range(len(correos) - 1):
    for j in range(len(correos) - i - 1):
        if correos[j] > correos[j + 1]:
            correos[j], correos[j + 1] = correos[j + 1], correos[j] 

print("Correos ordenados por riesgo:", correos)
