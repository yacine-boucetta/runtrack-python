class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("L'œuvre de", self.prenom, self.nom, ":")
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        print(self.prenom, self.nom, "a écrit le livre", titre)



auteur1 = Auteur("Verschaere", "Damien")
auteur1.ecrireUnLivre("Les test de python ")
auteur1.ecrireUnLivre("il fait froid ")
auteur1.listerOeuvre()

livre1 = Livre("Arthur et Toto", auteur1)
livre1.print()
auteur1.listerOeuvre()