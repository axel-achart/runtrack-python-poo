# Job 05 : Coordonnés d'un point qui bouge

# Création de la classe Point
class Point:
    # Constructeur Initialisation
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Méthode d'affichage des points
    def afficherLesPoints(self):
        print(f"x : {self.x}, y : {self.y}")
    
    # Méthode d'affichage de x
    def afficherX(self):
        print(f"x : {self.x}")
    
    # Méthode d'affichage de y
    def afficherY(self):
        print(f"y : {self.y}")

    # Méthode de changement de x
    def changerX(self):
        self.x = 50
    
    # Méthode de changement de y
    def changerY(self):
        self.y = 50

# Instancier la classe Point en 0, 0
mon_point = Point(0, 0)

# Afficher les points
mon_point.afficherLesPoints()

# Afficher x
mon_point.afficherX()
# Afficher y
mon_point.afficherY()
# Changer x et y
mon_point.changerX()
mon_point.changerY()

# Re-Afficher les points
mon_point.afficherLesPoints()