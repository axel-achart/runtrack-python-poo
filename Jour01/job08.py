# Job 08 : Calculs et informations d'un cercle

# Importer la librairie math
from math import *

# Création de la classe Cercle
class Cercle:
    # Constructeur Initialisation
    def __init__(self, rayon):
        self.rayon = rayon
        self.numero = 0

    # Méthode pour passer au cercle suivant
    def next_cercl(self):
        self.numero += 1
    
    # Méthode pour modifier le rayon
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    # Méthode pour calculer la circonférence
    def circonference(self):
        return 2 * pi * self.rayon

    # Méthode pour calculer l'aire
    def aire(self):
        return pi * (self.rayon ** 2)

    # Méthode pour calculer le diamètre
    def diametre(self):
        return 2 * self.rayon
    
    # Méthode pour afficher les informations du cercle
    def afficherInfos(self):
        print(f"Informations du cercle n°{self.numero}: ")
        print(f"Rayon : {self.rayon} cm")
        print(f"Circonférence : {self.circonference()} cm")
        print(f"Aire : {self.aire()} cm^2")
        print(f"Diamètre : {self.diametre()} cm")
        print()

# Instancier la classe Cercle avec rayon 4
mon_cercle = Cercle(4)
# Afficher les informations du cercle
mon_cercle.afficherInfos()

# Passer au cercle suivant
mon_cercle.next_cercl()

# Changer le rayon du cercle
mon_cercle.changerRayon(7)
# Afficher les informations du nouveau cercle
mon_cercle.afficherInfos()