# Job 09 : Informations, Calculs et modifications d'un produit

# Création de la classe Produit
class Produit:
    # Constructeur Initialisation
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    # Méthode de calcul du prix TTC
    def CalculerPrixTTC(self):
        return self.prixHT + self.TVA
    
    # Méthode d'affichage des informations
    def afficher(self):
        return self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()


    # Méthode de renommage du produit
    def renomme(self, nom):
        self.nom = nom
    
    # Méthode de changement de prix
    def changerPrix(self, prixHT):
        self.prixHT = prixHT

# Instancier la classe Produit avec un shampoing à 10€ HT et 3€ de TVA
shampoing = Produit("Shampoing", 10, 3)
print(shampoing.afficher())
# Renommer le shampoing + Changer le prix 10€ -> 15€
shampoing.renomme("Shampoing n°2")
shampoing.changerPrix(15)
print(shampoing.afficher())

print()

# Instancier la classe Produit avec un gel douche à 5€ HT et 4€ de TVA
gel_douche = Produit("Gel Douche", 5, 4)
print(gel_douche.afficher())
# Renommer le gel douche + Changer le prix 5€ -> 8€
gel_douche.renomme("Gel Douche n°2")
gel_douche.changerPrix(8)
print(gel_douche.afficher())