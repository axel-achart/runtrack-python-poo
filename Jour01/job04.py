# Job 04 : Nouvelle classe pour une personne

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(prenom, nom):
        print(f"Je suis {prenom} {nom}")


Personne.SePresenter("John", "Doe")
Personne.SePresenter("Jean", "Dupond")