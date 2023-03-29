mot = input("Entrez un mot sans espace ni caractère spécial : ")
n = len(mot)
letters = sorted(list(set(mot)))
permuts = []

# Générer toutes les permutations possibles du mot original
def permute(prefix, reste):
    if len(reste) == 0:
        permuts.append(prefix)
    else:
        for i in range(len(reste)):
            permute(prefix + reste[i], reste[:i] + reste[i+1:])

permute("", mot)

# Trouver la permutation la plus proche dans l'ordre alphabétique
plus_proche = mot
for p in permuts:
    if p > mot and (plus_proche == mot or p < plus_proche):
        plus_proche = p

print("Le mot le plus proche dans l'ordre alphabétique est :", plus_proche)
