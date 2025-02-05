# Job 02 : Comptes Bancaires, opérations (virement, versement, retrait)

# Classe CompteBancaire
class CompteBancaire:
    # Constructeur Initialisation
    def __init__(self, numcompte, nom, prenom, solde):
        self.__numcompte = numcompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = True  # Autorisation de découvert

    # Méthode afficher les informations du compte
    def afficher(self):
        print(f"Numéro de compte : {self.__numcompte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        self.afficherSolde()

    # Méthode afficher le solde du compte
    def afficherSolde(self):
        print(f"Solde : {self.__solde}€")

    # Méthode versement
    def versement(self, montantv):
        if montantv > 0:
            self.__solde += montantv
            print(f"VERSEMENT de {montantv}€ effectué.")
        else:
            print("Le montant du versement doit être positif.")

    # Méthode retrait
    def retrait(self, montantr):
        if montantr > 0 and (self.decouvert == True or montantr <= self.__solde):
            self.__solde -= montantr
            print(f"RETRAIT de {montantr}€ effectué.")
        else:
            print("Fonds insuffisants pour effectuer ce retrait.")

    # Méthode agios (interets quand découvert)
    def agios(self):
        if self.decouvert == True and self.__solde < 0:
            taux_agios = 0.2  # 20% d'agios
            self.__solde *= taux_agios
            print("AGIOS appliqués.")
        return self.__solde

    # Méthode virement
    def virement(self, compte_destinataire, montant):
        if montant > 0 and (self.decouvert == True or montant <= self.__solde):
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"VIREMENT de {montant}€ effectué vers {compte_destinataire.__nom} {compte_destinataire.__prenom}.")
        else:
            print("Virement impossible : fonds insuffisants.")

# Création des comptes
Hippolyte = CompteBancaire("1", "GESLAIN", "Hippolyte", 15000)
Kyllian = CompteBancaire("2", "LARCHER", "Kyllian", -1000)

# Affichage initial
Hippolyte.afficher()
Hippolyte.versement(100)
Hippolyte.afficherSolde()
Hippolyte.retrait(50)
Hippolyte.afficherSolde()

print()

# Informations du compte Kyllian 
Kyllian.afficher()

# Virement de Hippolyte vers Kyllian
Hippolyte.virement(Kyllian, 1000)

# Affichage final du compte Kyllian
Kyllian.afficherSolde()