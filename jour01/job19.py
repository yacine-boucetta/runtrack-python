def draw_rectangle(width, height):
    # Dessine la ligne supérieure du rectangle
    print("-" * width)

    # Dessine les lignes intermédiaires du rectangle
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessine la ligne inférieure du rectangle
    print("-" * width)

# Demande à l'utilisateur de saisir la largeur et la hauteur du rectangle
width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))

# Dessine le rectangle en utilisant les paramètres saisis par l'utilisateur
draw_rectangle(width, height)
