class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT + self.TVA
    
    def afficher(self):
        return self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()


    def renomme(self, nom):
        self.nom = nom
    
    def changerPrix(self, prixHT):
        self.prixHT = prixHT


    def infos(self):
        return self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()


shampoing = Produit("Shampoing", 10, 3)
print(shampoing.afficher())
shampoing.renomme("Shampoing n°2")
shampoing.changerPrix(15)
print(shampoing.afficher())

print()

gel_douche = Produit("Gel Douche", 5, 4)
print(gel_douche.afficher())
gel_douche.renomme("Gel Douche n°2")
gel_douche.changerPrix(8)
print(gel_douche.afficher())