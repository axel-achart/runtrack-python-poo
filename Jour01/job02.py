# Job 02 : Afficher en console les valeurs de nombre 1 et 2

# Création de la classe Operation
class Operation:
    # Constructeur Initialisation
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instancier la classe Operation
operation = Operation()

# Pour afficher les valeurs nombre 1 et 2
print(f"Le nombre1 est {operation.nombre1}")
print(f"Le nombre2 est {operation.nombre2}")