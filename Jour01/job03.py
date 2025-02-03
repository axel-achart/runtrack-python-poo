# Job 03 : Addition et affichage du résultat

# Création de la classe Operation
class Operation:
    # Constructeur Initialisation
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # Méthode addition
    def addition(self):
        return self.nombre1 + self.nombre2

# Instancier la classe Operation
operation = Operation()

# Afficher la phrase et le calcul de l'addition
print(f"L'addition de {operation.nombre1} et {operation.nombre2} est {operation.addition()}")