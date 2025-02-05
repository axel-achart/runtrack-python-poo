# Job 05 : Jeu de combat

# Classe Personnage
class Personnage:
    # Constructeur Initialisation
    def __init__(self, nom, vie):
        self.nom = nom  # str
        self.vie = vie  # int

    # Méthode personnage attaqué (subit des dégats)
    def attaqué(self, degats):
        self.vie = max(0, self.vie - degats)
        print(f"Dégats infligés de {degats} points, vie restante {self.vie}PV")
        return self.vie


# Classe Jeu
class Jeu:
    niveau = ""

    # Méthode Choisir le Niveau
    def choisirNiveau(self):
        while True:
            try:
                difficulte = int(input("\nChoisissez la difficulté (1. easy/2. medium/3. hard) : "))
                if difficulte == 1:
                    self.niveau = "Easy"
                    print("Mode Easy\n")
                    return self.niveau
                elif difficulte == 2:
                    self.niveau = "Medium"
                    print("Mode Medium\n")
                    return self.niveau
                elif difficulte == 3:
                    self.niveau = "Hard"
                    print("Mode Hard\n")
                    return self.niveau
            except ValueError:
                print("Veuillez entrer un chiffre valide.")

    # Méthode Lancer le Jeu, et défini les personnages en fonction des niveaux
    def lancerJeu(self):
        if self.niveau == "Easy":
            joueur = Personnage("Dracaufeu", 100)
            ennemi = Personnage("Pichu", 50)
        elif self.niveau == "Medium":
            joueur = Personnage("Dracaufeu", 150)
            ennemi = Personnage("Pikachu", 150)
        elif self.niveau == "Hard":
            joueur = Personnage("Dracaufeu", 200)
            ennemi = Personnage("Raichu", 250)
        return joueur, ennemi
    
    # Méthode Vérification de la santé des personnages et vérifie qui a gagné
    def VerifSante(self, joueur, ennemi):
        print(f"La santé de {joueur.nom} est de {joueur.vie}")
        print(f"La santé de {ennemi.nom} est de {ennemi.vie}")
        self.QuiAGagne(joueur, ennemi)

    # Méthode Qui a gagné appelé dans "VerifSante"
    def QuiAGagne(self, joueur, ennemi):
        if joueur.vie == 0 and ennemi.vie > 0:
            print("\nL'ennemi a gagné !")
        elif ennemi.vie == 0 and joueur.vie > 0:
            print("\nLe joueur a gagné !")


# Récuperation de la classe Jeu
RUN = Jeu()

# Lancement du jeu et choisir un niveau
RUN.choisirNiveau()

# Récupération des personnages
joueur, ennemi = RUN.lancerJeu()

# Vérification de la santé des personnages
RUN.VerifSante(joueur, ennemi)

# Joueur attaqué
joueur.attaqué(130)

# Ennemi attaqué
ennemi.attaqué(160)

# Vérification de la santé des personnages après attaques
RUN.VerifSante(joueur, ennemi)