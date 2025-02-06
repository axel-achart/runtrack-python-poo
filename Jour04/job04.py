# Job 04 : Les formes, rectangles


class Forme:
    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur


rect = Rectangle(10, 5)
print(rect.aire())