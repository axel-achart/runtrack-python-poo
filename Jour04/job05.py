# Job 05 : Les formes et calculs

from math import *

class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius    # Rayon du cercle

    def aire(self):
        return pi * (self.radius**2)
    
my_rect = Rectangle(10, 5)
print(f"Aire du rectangle : {my_rect.aire()}")

my_cercl = Cercle(9)
print(f"Aire du cercle : {my_cercl.aire()}")