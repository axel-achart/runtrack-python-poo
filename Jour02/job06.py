# Job 06 : Commandes d'un restauration, ce qui se trouve dedans, le prix, le status

# Classe Commande
class Commande:
    # Constructeur Initialisation
    def __init__(self, numcom):
        self.__numcom = numcom  # Numéro de commande
        self.__listeplat = {
            "nom" : [],
            "prix" : [],
            "statut" : ""
        }
        self.__price = 0 # Prix total de la commande

    # Ajouter un plat a la commande
    def add_com(self):
        while True:
            try:
                new_name = str(input("\nEntrez le nom du plat à ajouter : "))
                new_prix = int(input("Entrez le prix du plat à ajouter : "))
                self.__listeplat["nom"].append(new_name)
                self.__listeplat["prix"].append(new_prix)
                self.__listeplat["statut"] = 'En cours'
                return
            except ValueError:
                print("Plat incorrect")

    # Effacer la commande
    def cancel_com(self):
        self.__listeplat.clear()
        
    # Calculer le total d'une commande privée
    def calcul_pv(self):
        self.__price = sum(self.__listeplat["prix"])
        return self.__price

    # Calculer la TVA
    def calcul_tva(self):
        return 0.2 * self.__price

    # Afficher une commande et ses détails
    def display_com(self):
        print()
        print(f"Numéro : {self.__numcom}") # OK
        print(f"Les plats : {self.__listeplat["nom"]}") # OK
        print(f"Le prix total à payer : {self.calcul_pv()}€")
        print(f"TVA : {self.calcul_tva()}€") # OK
        print(self.__listeplat["statut"])
        print()

# Fonction main
def main():
    run = True
    numero = 1
    commande = Commande(numero)
    while run:
        # Ajouter un plat et son prix à la commande
        commande.add_com()

        # Afficher la commande
        commande.display_com()

        # Si oui, sort de la boucle et efface la commande
        leave = input("Voulez-vous finir la commande ? (y/n) : ")
        if leave == 'y':
            commande.cancel_com()
            run = False
            new_com()

# Fonction si la commande est fini, possibilité de créer une nouvelle commande
def new_com():
    new_command = input("\nVoulez-vous commencer une nouvelle commande ? (y/n) : ")
    if new_command == 'y':
        main()

# Programme execute
if __name__ == '__main__':
    main()