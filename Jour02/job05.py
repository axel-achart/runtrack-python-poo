# Job 05 : Définition d'une voiture avec son état de marche

# Classe Voiture
class Voiture:
    # Constructeur Initialisation
    def __init__(self, marque, modele, annee, kilom):
        self.__marque = marque
        self.__modele = modele 
        self.__annee = annee
        self.__kilom = kilom
        self.en_marche = False
        self.__reservoir = 50
    
    # Accesseurs et Mutateurs
    def accesseurs(self):
        return self.__marque, self.__modele, self.__annee, self.__kilom, self.en_marche
    
    def mut_marque(self, marque):
        self.__marque = marque
    def mut_modele(self, modele):
        self.__modele = modele
    def mut_annee(self, annee):
        self.__annee = annee
    def mut_kilom(self, kilom):
        self.__kilom = kilom
    def mut_en_marche(self):
        if not self.en_marche:
            self.en_marche = True
        else:
            self.en_marche = False
    
    # Démarrer la voiture si l'essence est suffisant
    def demarrer(self):
        if self._verifier_plein() > 5:
            print("Voiture démarre")
            self.en_marche = True
        else:
            print("Pas assez d'essence...")

    # Arrêter la voiture
    def arreter(self):
        print("Voiture s'arrête")
        self.en_marche = False

    # Vérifier si le réservoir est rempli ou non et combien d'essence
    def _verifier_plein(self):
        return self.__reservoir

# Initialisation d'une voiture
ma_gov = Voiture("Ford", "Mustang GT500", "2024", 15000)
print(ma_gov.accesseurs())

# Modifications de l'année de la voiture
ma_gov.mut_annee("2025")
print(ma_gov.accesseurs())

# Démarrer la voiture
ma_gov.demarrer()
print(ma_gov.accesseurs())

# Arrêter la voiture
ma_gov.arreter()
print(ma_gov.accesseurs())