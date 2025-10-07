def apple_and_orange(s, t, a, b, mazanas, naranjas):
    manzanas_cayendo = [a + d for d in mazanas]
    naranjas_cayendo = [b + d for d in naranjas]
    manzanas_en_casa = sum(1 for d in manzanas_cayendo if s <= d <= t)
    naranjas_en_casa = sum(1 for d in naranjas_cayendo if s <= d <= t)
    return manzanas_en_casa, naranjas_en_casa
print(apple_and_orange(7, 11, 5, 15, [-2, 2, 1], [5, -6]))
#7-11 arbol de mazanas
#5-15 arbol de naranjas
#-2,2,1 caen manzanas
#5,-6 caen naranjas
#1-1 cuantas manzanas y naranjas caen en la casa