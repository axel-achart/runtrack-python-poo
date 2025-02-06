# Job 07 : Jeu du Blackjack

import random


class Carte:
    def __init__(self):
        self.valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi", "AS"]
        self.couleurs = ["Coeur", "Carreaux", "Pique", "Trèfle"]
        self.valeur = random.choice(self.valeurs)
        self.couleur = random.choice(self.couleurs)

    def afficherCarte(self):
        print(f"{self.valeur} de {self.couleur} ({self.pointsParCartes()} points)")

    def pointsParCartes(self):
        if self.valeur == "Valet" or self.valeur == "Reine" or self.valeur == "Roi":
            self.points = 10
            return self.points
        elif self.valeur == "AS":
            self.points = int(input("Voulez-vous prendre 1 ou 11 points ? : "))
            return self.points
        elif self.valeur == "2":
            self.points = 2
            return self.points
        elif self.valeur == "3":
            self.points = 3
            return self.points
        elif self.valeur == "4":
            self.points = 4
            return self.points
        elif self.valeur == "5":
            self.points = 5
            return self.points
        elif self.valeur == "6":
            self.points = 6
            return self.points
        elif self.valeur == "7":
            self.points = 7
            return self.points
        elif self.valeur == "8":
            self.points = 8
            return self.points
        elif self.valeur == "9":
            self.points = 9
            return self.points
        elif self.valeur == "10":
            self.points = 10
            return self.points
        

class Jeu:
    def __init__(self):
        self.paquet = []    # Avec 52 cartes

    # Méthode Lancement du jeu
    def debut(self):
        print("\nDébut du jeu")

    # Méthode pour recevoir les 2 cartes
    def accesseurs(self):
        pass

    # Méthode affichage des cartes attribuées
    def afficherCartesAttribués(self):
        pass

    # Méthode pour choisir entre 'prendre' ou 'passer'
    def choisir(self):
        pass

    # Méthode le croupier prend des cartes jusqu'à au moins 17pts
    def boucleCroupier(self):
        pass

    # Méthode pour retourner le score de chacun
    def scores(self):
        pass

    # Méthode pour vérifier qui a gagné
    def verifGagner(self):
        pass


premiere_carte = Carte()
deuxieme_carte = Carte()

premiere_carte.afficherCarte()
deuxieme_carte.afficherCarte()