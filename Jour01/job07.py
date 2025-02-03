class Personnage:
    def __init__(self):
        self.x = 0  # Coordonnné x du joueur
        self.y = 0  # Coordonné y du joueur

    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1
    
    def position(self):
        return self.x, self.y