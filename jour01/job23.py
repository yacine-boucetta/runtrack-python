def draw_triangle(height):
    # Dessine la première ligne du triangle
    print("_" * (height - 1) + "/" + "_" * (height - 1))

    # Dessine les lignes intermédiaires du triangle
    for i in range(1, height - 1):
        print(" " * (height - i - 1) + "/" + " " * (2 * i - 1) + "\\")

    # Dessine la ligne inférieure du triangle
    print("/" + "_" * (2 * height - 2) + "\\")

# Demande à l'utilisateur de saisir la hauteur du triangle
height = int(input("Entrez la hauteur du triangle : "))

# Dessine le triangle en utilisant la hauteur saisie par l'utilisateur
draw_triangle(height)
