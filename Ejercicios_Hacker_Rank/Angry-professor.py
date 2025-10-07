def angryprofessor(k, a):
    en_tiempo_estudiantes = 0
    for llegada in a:
        if llegada <= 0:
            en_tiempo_estudiantes += 1
    if en_tiempo_estudiantes < k:
        return "Si" #la clase se cancela
    else:
        return"No" #la clase no se cancela

print(angryprofessor(3, [-2, -1, 0, 1, 2,])), 