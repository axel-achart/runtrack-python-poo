# Job 06 : Commandes d'un restauration, ce qui se trouve dedans, le prix, le status

# Classe Commande
class Commande:
    # Constructeur Initialisation
    def __init__(self, numcom):
        self.__numcom = numcom
        self.__listeplat = {}  # En dictionnaire (noms de plats, prix, status)
        self.__statut = ['En cours', 'Terminée', 'Annulée']

    # Ajouter un plat a la commande
    def add_com(self):
        try:
            new_plat = str(input("Entrez le plat à ajouter : "))
            self.__listeplat.append(new_plat)
        except ValueError:
            print("Nom de plat incorrect")
    
    # Annuler une commande
    def cancel_com(self):
        pass
        
    # Calculer le total d'une commande privée
    def calcul_pv(self):
        pass

    # Afficher une commande avec son total à payer
    def display_com(self):
        pass

    # Calculer la TVA
    def calcul_tva(self):
        pass