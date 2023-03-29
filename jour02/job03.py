class Personne : 
    def __init__(self,nom,prenom) :
        self.nom=nom
        self.prenom=prenom



class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre=[]
    def ecrireLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre



class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = {}
    def inventaire(self):
        print( self.prenom, self.nom, "possede")
        for titre, quantite in self.collection.items():
            print("Livre :", titre, ", Quantité :", quantite)

class Livre:
    def __init__(self,titre,auteur):
        self.titre=titre
        self.auteur=auteur
        

class Bibliotheque : 
    def __init__(self,nom) :
        self.nom=nom
        # initialisé à vide pour chaque instance de la class
        self.catalogue={}
    
    def acheterLivre(self,auteur,titre,quantite):
        for livre in auteur.oeuvre:
            if livre.titre==titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print("Nous avons acheté",quantite,"du livre",titre,"ecrit par",auteur.nom,auteur.prenom)
                return 
        print("le livre",titre,"ecrit par",auteur.nom,auteur.prenom,"n'existe pas pas dans nos fichiers")
    
    def inventaire(self):
        for titre,quantite in self.catalogue.items():
            print("nous avons :",quantite,"de",titre)
    
    def louer(self,client,titre):
        if titre in self.catalogue and self.catalogue[titre]>0:
            if titre in client.collection:
                client.collection[titre]+=1
            else : 
                    client.collection[titre]=1
            self.catalogue[titre] -= 1
            print(client.nom,client.prenom,"a loué",titre)
        else:
            print("aucun stock de",titre)
    
    def rendreLivres(self, client):
        for titre, quantite in client.collection.items():
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
            print("recuperation de", quantite, " du livre", titre, "louer par ", client.nom, client.prenom)
        client.collection.clear()


# Instanciation des auteurs et création de livres
auteur1 = Auteur("Boucetta", "Yacine")
auteur1.ecrireLivre("Yacine apprend a nager dans la mediteranée")
auteur1.ecrireLivre("Yacine et le point de deal")
auteur2 = Auteur("Diop", "Raphael")
auteur2.ecrireLivre("Etre un bounty ++")

# Création d'une bibliothèque et achat de livres
bibliotheque = Bibliotheque("Bibliothèque Test")
bibliotheque.acheterLivre(auteur1, "Yacine apprend a nager dans la mediteranée", 5)
bibliotheque.acheterLivre(auteur1, "Yacine et le point de deal", 3)
bibliotheque.acheterLivre(auteur2, "Etre un bounty ++", 2)

# Création de clients et location de livres
client1 = Client("Lepen", "Marine")
client2 = Client("TDelacase", "Thomas")
bibliotheque.louer(client1, "Yacine apprend a nager dans la mediteranée")
bibliotheque.louer(client1, "Etre un bounty ++")
bibliotheque.louer(client2, "Yacine et le point de deal")
bibliotheque.louer(client2, "Etre un bounty ++")

# Affichage des inventaires
bibliotheque.inventaire()
client1.inventaire()
client2.inventaire()

# Rendre les livres
bibliotheque.rendreLivres(client1)
bibliotheque.rendreLivres(client2)

# Affichage des inventaires après le retour des livres
bibliotheque.inventaire()
client1.inventaire()
client2.inventaire()