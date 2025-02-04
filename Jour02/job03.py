# Job 03 : Ajout de la disponibilités et emprunt/rendu du livre

# Classe Livre
class Livre:
    # Constructeur Initialisation
    def __init__(self, titre, auteur, nbrepage):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrepage = nbrepage
        self.__disponible = True

    # Récuperer les valeurs
    def accesseurs(self):
        return self.__titre, self.__auteur, self.__nbrepage
    
    # Modifier les valeurs
    def mutateurs(self, titre, auteur, nbrepage):
        self.__titre = titre
        self.__auteur = auteur
        if nbrepage > 0 and isinstance(nbrepage,(int)):
            self.__nbrepage = nbrepage
        else:
            print("Nombre de page incorrect, utilisez un entier positif. Les valeurs ne sont pas changés.")

    # Vérifier si le livre est dispo ou non (True/False)
    def verification(self):
        if self.__disponible:
            return True
        else:
            return False
    
    # Vérifie si il est disponible, si oui il est emprunter
    def emprunter(self):
        if Livre.verification(self):
            self.__disponible = False
            print("Livre emprunté avec succès !")
        else:
            print("\nLivre non disponible\n")

    # Vérifie si il est bien emprunté, si oui il devient disponible car il est rendu
    def rendre(self):
        if not Livre.verification(self):
            self.__disponible = True
            print("Livre rendu avec succès !")
        else:
            print("\nLivre non emprunté, il ne peut être rendu")


print("\nLe livre est disponible.")

# Livre de base
new_livre = Livre("La romance", "Axel", 200)
print(new_livre.accesseurs())

# Emprunt du livre verification
print(new_livre.verification())

# Emprunt du livre
new_livre.emprunter()

# Vérification de l'emprunt
print(new_livre.verification())

# Rendu du livre
new_livre.rendre()