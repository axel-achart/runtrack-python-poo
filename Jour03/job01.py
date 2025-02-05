# Job 01 : Population de villes

# Classe Ville
class Ville:
    # Constructeur Initialisation
    def __init__(self, nomv, nbrehab):
        self.__nomv = nomv 
        self.__nbrehab = nbrehab
    
    # Méthode mutateur ajout d'un habitant
    def mutateur(self):
        self.__nbrehab += 1
    
    # Méthode afficher la population de la ville
    def afficher(self):
        print(f"Population de la ville de {self.__nomv} : {self.__nbrehab} habitants.")
    
    # Méthode mise à jour de la population de la ville
    def maj(self):
        print(f"Mise à jour de la population de la ville de {self.__nomv} {self.__nbrehab} habitants")

# Classe Personne
class Personne(Ville):
    # Constructeur Initialisation
    def __init__(self, nom, age, ville):
        self.__nom = nom 
        self.__age = age 
        self.__ville = ville

    # Méthode ajouter une population
    def ajouterPopulation(self):
        self.__ville.mutateur()


# Création des villes
Paris = Ville("Paris", 1000000)
Paris.afficher()
Marseille = Ville("Marseille", 861635)
Marseille.afficher()

# Création des personnes
John = Personne("John", "45", Paris)
John.ajouterPopulation()

Myrtille = Personne("Myrtille", "4", Paris)
Myrtille.ajouterPopulation()

Chloé = Personne("Chloé", "18", Marseille)
Chloé.ajouterPopulation()

# Mise à jour des populations
Paris.maj()
Marseille.maj()