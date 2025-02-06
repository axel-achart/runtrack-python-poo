# Job 07 : Blackjack

import random

# Classe Carte
class Carte:
    # Constructeur Initialisation
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    # Afficher la carte
    def afficher(self):
        print(f"{self.valeur} de {self.couleur}")
    
    # Points de la carte
    def points(self):
        if self.valeur in ["Valet", "Reine", "Roi"]:
            return 10
        elif self.valeur == "AS":
            return 11  # Géré dans le calcul du score pour ajuster
        else:
            # Point de la carte en fonction de son numéro
            return int(self.valeur)

# Classe Jeu
class Jeu:
    # Constructeur Initialisation
    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi", "AS"]
        couleurs = ["Coeur", "Carreaux", "Pique", "Trèfle"]
        # Création du paquet de cartes
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        # Mélanger le paquet
        random.shuffle(self.paquet)
        # Initialisation des mains
        self.joueur_main = []
        self.croupier_main = []
    
    # Distribuer les cartes et supprimer du paquet la carte prise
    def distribuer_cartes(self):
        for _ in range(2):
            self.joueur_main.append(self.paquet.pop())
            self.croupier_main.append(self.paquet.pop())
    
    # Afficher la main
    def afficher_main(self, main, joueur):
        print(f"Main de {joueur}:")
        for carte in main:
            carte.afficher()
        print(f"Score: {self.calculer_score(main)}\n")
    
    # Calculer le score
    def calculer_score(self, main):
        score = sum(carte.points() for carte in main)
        as_count = sum(1 for carte in main if carte.valeur == "AS")
        
        while score > 21 and as_count:
            score -= 10  # L'As passe de 11 à 1
            as_count -= 1
        
        return score
    
    # Tour du joueur
    def tour_joueur(self):
        while True:
            self.afficher_main(self.joueur_main, "Joueur")
            if self.calculer_score(self.joueur_main) > 21:
                print("Vous avez dépassé 21, vous perdez !")
                return False
            choix = input("Voulez-vous une autre carte ? (o/n) : ").lower()
            if choix == 'o':
                self.joueur_main.append(self.paquet.pop())
            else:
                break
        return True
    
    # Tour du croupier
    def tour_croupier(self):
        while self.calculer_score(self.croupier_main) < 17:
            self.croupier_main.append(self.paquet.pop())
        self.afficher_main(self.croupier_main, "Croupier")
    
    # Déterminer le gagnant
    def determiner_gagnant(self):
        joueur_score = self.calculer_score(self.joueur_main)
        croupier_score = self.calculer_score(self.croupier_main)
        
        if joueur_score > 21:
            print("Le croupier gagne !")
        elif croupier_score > 21 or joueur_score > croupier_score:
            print("Vous gagnez !")
        elif joueur_score < croupier_score:
            print("Le croupier gagne !")
        else:
            print("Égalité !")
    
    # Jouer
    def jouer(self):
        print("\nDébut du Blackjack !")
        self.distribuer_cartes()
        if self.tour_joueur():
            self.tour_croupier()
            self.determiner_gagnant()

# Lancer une partie
jeu = Jeu()
jeu.jouer()