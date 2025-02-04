# Job 01 : Attributs privés et accesseurs et mutateurs

# Classe Rectangle
class Rectangle:
    # Constructeur Initialisation
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Accesseurs et Mutateurs
    def accesseurs(self):
        return self.__longueur, self.__largeur
    def mutateurs(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

# Rectangle 10 x 5
my_rect = Rectangle(10, 5)
print(my_rect.accesseurs())

# Rectangle 20 x 10
my_rect.mutateurs(20, 10)
print(my_rect.accesseurs())