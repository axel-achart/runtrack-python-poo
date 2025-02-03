# Job 07 : Coordonnnées du joueur + Mouvement des coordonnées

# Création de la classe Personnage
class Personnage:
    # Constructeur Initialisation
    def __init__(self):
        self.x = 0  # Coordonnné x du joueur
        self.y = 0  # Coordonné y du joueur

    # Méthode de déplacement à gauche
    def gauche(self):
        self.x -= 1
    
    # Méthode de déplacement à droite
    def droite(self):
        self.x += 1
    
    # Méthode de déplacement en bas
    def bas(self):
        self.y += 1

    # Méthode de déplacement en haut
    def haut(self):
        self.y -= 1
    
    # Méthode de position pour retourner les 2 coordonnées mises à jour
    def position(self):
        return self.x, self.y