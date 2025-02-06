# Job 03 : 


class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return self.__longueur*2 + self.__largeur*2
    
    def surface(self):
        return self.__longueur  * self.__largeur

    def assesseurs(self):
        return self.__longueur, self.__largeur
    
    def mutateurs(self, new_longueur, new_largeur):
        self.__longueur = new_longueur
        self.__largeur = new_largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, hauteur, longueur, largeur):
        self.hauteur = hauteur
        super().__init__(longueur, largeur)
    
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.hauteur
    

rectangle_2d = Rectangle(10, 4)
print(f"Perimetre : {rectangle_2d.perimetre()}m")
print(f"Aire : {rectangle_2d.surface()}m^2")
print(f"Stats : {rectangle_2d.assesseurs()}")

rectangle_2d.mutateurs(100, 50)
print(f"Perimetre : {rectangle_2d.perimetre()}m")
print(f"Aire : {rectangle_2d.surface()}m^2")
print(f"Stats : {rectangle_2d.assesseurs()}")

rectangle_3d = Parallelepipede(25, 100, 50)
print(f"Volume : {rectangle_3d.volume()}m^3")