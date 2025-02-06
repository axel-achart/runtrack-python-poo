# Job 02 : Interactions et Paroles d'eleve et professeur


class Personne:
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print()
        print(f"Age : {self.age}")
    
    def bonjour(self):
        print("\nHello")
    
    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("\nJe vais en cours")

    def afficherAge(self):
        print()
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def get_matiere(self):
        return self.__matiereEnseignee
    
    def enseigner(self):
        print("\nLe cours va commencer")


Kyllian = Eleve()
Kyllian.bonjour()
Kyllian.allerEnCours()
Kyllian.modifierAge(15)
Kyllian.afficherAge()

Akram = Professeur("IA")
Akram.modifierAge(40)
Akram.bonjour()
Akram.enseigner()
Akram.afficherAge()