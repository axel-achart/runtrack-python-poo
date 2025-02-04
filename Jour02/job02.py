# Job 02 : Livre avec modification des attributs

# Classe Livre
class Livre:
    # Constructeur Initialisation
    def __init__(self, titre, auteur, nbrepage):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrepage = nbrepage

    # Accesseurs et Mutateurs
    def accesseurs(self):
        return self.__titre, self.__auteur, self.__nbrepage
    def mutateurs(self, titre, auteur, nbrepage):
        self.__titre = titre
        self.__auteur = auteur
        if nbrepage > 0 and isinstance(nbrepage,(int)):
            self.__nbrepage = nbrepage
        else:
            print("Nombre de page incorrect, utilisez un entier positif. Les valeurs ne sont pas changés.")

# Livre
mon_livre = Livre("L'Histoire", "Axel", 200)
print(mon_livre.accesseurs())

# Modifications du livre impossibles
mon_livre.mutateurs("Son Histoire", "Pas Axel", -10)
mon_livre.mutateurs("Son Histoire", "Pas Axel", 250.75)