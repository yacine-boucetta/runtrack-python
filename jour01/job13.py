

nbrs = []
for i in range(10):
    nombre = int(input("Entrez un nombre entier : "))
    nbrs.append(nombre)



#fonction de triage 
nbrs.sort()
print("Voici les nombres triés par ordre croissant!")
for nombre in nbrs:
    print(nombre)
