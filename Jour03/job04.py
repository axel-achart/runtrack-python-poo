# Job 04 : Joueur de foot

# Classe Joueur
class Joueur:
    # Constructeur Initialisation
    def __init__(self, nom, numero, position, but_marque, passe_d, cart_jaune, cart_rouge):
        self.nom = nom 
        self.numero = numero 
        self.position = position
        self.but_marque = but_marque
        self.passe_d = passe_d
        self.cart_jaune = cart_jaune
        self.cart_rouge = cart_rouge

    # Méthode marquer un but
    def marquerUnBut(self):
        self.but_marque += 1
        return self.but_marque
    
    # Méthode effectuer une passe décisive
    def effectuerUnePasseDecisive(self):
        self.passe_d += 1
        return self.passe_d

    # Méthode recevoir un carton jaune
    def recevoirUnCartonJaune(self):
        self.cart_jaune += 1
        return self.cart_jaune
    
    # Méthode recevoir un carton rouge
    def recevoirUnCartonRouge(self):
        self.cart_rouge += 1
        return self.cart_rouge

    # Méthode afficher les statistiques du joueur
    def afficherStatistiques(self):
        print()
        print(f"Statistiques de {self.nom} n°{self.numero} :")
        print(f"{self.but_marque} buts marqués")
        print(f"{self.passe_d} passes décisives")
        print(f"{self.cart_jaune} cartons jaunes reçus")
        print(f"{self.cart_rouge} cartons rouges reçus")
    
# Classe Equipe
class Equipe:
    # Constructeur Initialisation
    def __init__(self, nom_equipe):
        self.nom_equipe = nom_equipe
        self.liste_joueurs = []
    
    # Méthode ajouter un joueur à l'équipe
    def ajouterJoueur(self, add_joueur):
        self.liste_joueurs.append(add_joueur)
        print(f"Nouveau joueur ajouté à l'effectif : {add_joueur.nom}")

    # Méthode afficher les statistiques des joueurs de l'équipe
    def AfficherStatistiquesJoueurs(self):
        if self.liste_joueurs:
            for i in self.liste_joueurs:
                Joueur.afficherStatistiques(i)
        else:
            print("Equipe vide")
    
    # Méthode mettre à jour les statistiques du joueur
    def mettreAJourStatistiquesJoueur(self):
        print()
        print(f"Nouvelles Statistiques de {self.nom} n°{self.numero} :")
        print(f"{self.but_marque} buts marqués")
        print(f"{self.passe_d} passes décisives")
        print(f"{self.cart_jaune} cartons jaunes reçus")
        print(f"{self.cart_rouge} cartons rouges reçus")


# Création d'une équipe
mon_equipe = Equipe("FC Ensues")

# Création de joueurs
Neymar = Joueur("Neymar", "10", "Milieu Offensif", 10, 2, 0, 0)
Mbappé = Joueur("Mbappé", "9", "Avant-centre", 15, 5, 0, 0)
Barcola = Joueur("Barcola", "29", "Ailier Gauche", 25, 10, 0, 0)

# Ajout des joueurs à l'équipe
mon_equipe.ajouterJoueur(Neymar)
mon_equipe.ajouterJoueur(Mbappé)
mon_equipe.ajouterJoueur(Barcola)

# Affichage des statistiques des joueurs
Neymar.afficherStatistiques()
Mbappé.afficherStatistiques()
Barcola.afficherStatistiques()

# Match
Neymar.recevoirUnCartonJaune()
Mbappé.marquerUnBut()
Barcola.effectuerUnePasseDecisive()
Neymar.marquerUnBut()
Mbappé.effectuerUnePasseDecisive()
Barcola.recevoirUnCartonJaune()
Neymar.recevoirUnCartonJaune()
Neymar.recevoirUnCartonRouge()
# Fin de Match

# Mise à jour des statistiques des joueurs en fin de match
mon_equipe.AfficherStatistiquesJoueurs()