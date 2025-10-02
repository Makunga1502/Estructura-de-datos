# Imagen 3x3 en escala de grises
image = [
    [  0,  64, 128],
    [192, 255, 192],
    [128,  64,   0]
]

def print_image(mat):
    for row in mat:
        print(" ".join(f"{v:3d}" for v in row))
    print()

print("Imagen original:")
print_image(image)

# Acceso al píxel central (fila 1, col 1 con índice base 0)
center = image[1][1]
print(f"Píxel central antes: {center}")

# Modificar el valor del píxel central
image[1][1] = 100
print("Imagen después de modificar el píxel central a 100:")
print_image(image)
