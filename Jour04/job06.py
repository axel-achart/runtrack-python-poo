# Job 06  : Les véhicules (voitures, motos)


class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele 
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modele : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}")
    
    def demarrer(self):
        print("Attention, je roule !")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
   
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("Attention, ça ronronne !")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("Attention, je cabre !")




mustang = Voiture("Ford", "Mustang", "2024", 40000)
mustang.informationsVehicule()
mustang.demarrer()
print()
africa = Moto("Yamaha", "Africa Twin", "2025", 15000)
africa.informationsVehicule()
africa.demarrer()