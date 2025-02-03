# Job 04 : Présenter une nouvelle personne

# Création de la classe Personne
class Personne:
    # Constructeur Initialisation
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Méthode de présentation
    def SePresenter(prenom, nom):
        print(f"Je suis {prenom} {nom}")

# Afficher la présentation de chaque personne
Personne.SePresenter("John", "Doe")
Personne.SePresenter("Jean", "Dupond")