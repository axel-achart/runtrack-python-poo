# Job 01 : Créer la classe avec le constructeur + Attributs + Instanciez votre première classe et imprimez l’objet en console.

class Operation:
    # Constructeur/Méthode
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instancier la classe Operation
operation=Operation()

# Pour afficher la variable qui a pris la classe Operation
print(operation)