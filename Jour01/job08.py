from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.numero = 0

    def next_cercl(self):
        self.numero += 1
    
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    def circonference(self):
        return 2 * pi * self.rayon

    def aire(self):
        return pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon
    
    def afficherInfos(self):
        print(f"Informations du cercle n°{self.numero}: ")
        print(f"Rayon : {self.rayon} cm")
        print(f"Circonférence : {self.circonference()} cm")
        print(f"Aire : {self.aire()} cm^2")
        print(f"Diamètre : {self.diametre()} cm")
        print()

mon_cercle = Cercle(4)
mon_cercle.afficherInfos()

mon_cercle.next_cercl()

mon_cercle.changerRayon(7)
mon_cercle.afficherInfos()