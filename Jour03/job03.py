# Job 03 : To Do List

# Classe Tache
class Tache:
    # Constructeur Initialisation
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.desc = description
        self.statut = statut    # A faire/Terminé

    # Méthode mettre sous forme de string
    def __str__(self):
        return f"{self.titre} - {self.desc}, {self.statut}"
    
# Classe ListeDeTaches
class ListeDeTaches:
    # Constructeur Initialisation
    def __init__(self):
        self.taches = []

    # Ajouter une tâche
    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée avec succès ({tache}) !")
    
    # Supprimer une tâche
    def supprimerTache(self):
        self.afficherListe()
        if self.taches:
            try:
                index = int(input(f"Entrez l'index de la tâche à supprimer (0 - {len(self.taches)-1}) : "))
                if 0 <= index < len(self.taches):
                    supprimee = self.taches.pop(index)
                    print(f"Tâche supprimée : {supprimee}")
                else:
                    print("Index invalide.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        else:
            print("Aucune tâche à supprimer.")

    # Signaler que la tâche est faite
    def marquerCommeFinie(self, index):
        if 0 <= index < len(self.taches):
            self.taches[index].statut = "Terminé"
            print(f"Tâche terminée : {self.taches[index]}")
        else:
            print("Index invalide.")

    # Retourne une liste de toutes les tâches
    def afficherListe(self):
        if self.taches:
            print("\n- - Liste des tâches - -")
            for i, tache in enumerate(self.taches):
                print(f"{i}. {tache}")
        else:
            print("Aucune tâche.")
    
    # Filtrer les tâches par rapport au statut et retourne cette liste (creer une liste spécifique)
    def filterListe(self):
        taches_a_faire = [t for t in self.taches if t.statut == "A faire"]
        if taches_a_faire:
            print("\nTâches à faire :")
            for tache in taches_a_faire:
                print(tache)
        else:
            print("\nToutes les tâches sont terminés !")

# Créer une liste de tâches
listeTaches = ListeDeTaches()

# Créer plusieurs tâches
menage = Tache("Faire ménage", "Aspirateur/Serpillère", "A faire")
nettoyer = Tache("Nettoyer Voiture", "Utiliser serviette", "A faire")

# Les ajouter a la listeDeTache
listeTaches.ajouterTache(menage)
listeTaches.ajouterTache(nettoyer)

# Supprimer une tâche
listeTaches.supprimerTache()

# Changer le statut
listeTaches.marquerCommeFinie(0)

# Afficher toutes les tâches
listeTaches.afficherListe()

# Afficher les tâches "A faire" seulement
listeTaches.filterListe()