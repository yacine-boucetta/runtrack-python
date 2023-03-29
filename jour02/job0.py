class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je m'appelle", self.prenom, self.nom)

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom



personne1 = Personne("Verschaere", "Damien")
personne2 = Personne("Diop", "Raphael")
personne3 = Personne("Boucetta", "Yacine")

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()

#accesseurs 
print(personne1.getNom())
print(personne3.getPrenom())

personne2.setPrenom("chouquette")
personne2.SePresenter()