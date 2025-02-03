# Job 01 : Afficher l'objet en console

# Création de la classe Operation
class Operation:
    # Constructeur Initialisation
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instancier la classe Operation
operation = Operation()

# Pour afficher la variable qui a pris la classe Operation
print(operation)