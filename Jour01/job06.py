# Job 06 : Définir un animal avec son age + vieillesse

# Création de la classe Animal
class Animal:
    # Constructeur Initialisation
    def __init__(self):
        self.age = 0
        self.prenom = ""

    # Méthode de vieillissement +1 an
    def vieillir(self):
        self.age += 1
    
    # Méthode pour renommer l'animal
    def nommer(self, prenom):
        self.prenom = prenom

# Instancier la classe Animal
singe = Animal()
# Afficher l'age de l'animal
print(f"L'age de l'animal {singe.age} ans")

# Vieillir l'animal  +1an
singe.vieillir()
# Afficher l'age de l'animal après vieillissement
print(f"L'age de l'animal {singe.age} ans")

# Renommer l'animal
singe.nommer("Singe Européen")
# Afficher le nouveau nom de l'animal
print(f"L'animal se nomme {singe.prenom}")