# Job 02 : Print en consol les valeur nombre 1 et 2

class Operation:
    # Constructeur/Méthode
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instancier la classe Operation
operation=Operation()

# Pour afficher les valeurs nombres
print(f"Le nombre1 est {operation.nombre1}")
print(f"Le nombre2 est {operation.nombre2}")