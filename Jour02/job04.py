# Job 04 : Système de notation d'élève avec attributs propre à l'élève

# Classe Student
class Student:
    # Constructeur Initialisation
    def __init__(self, nom, prenom, numetud):
        self.__nom = nom 
        self.__prenom = prenom
        self.__numetud = numetud
        self.__credits = 0
        self.__level = self._student_eval()
    
    # Ajouter des crédits par 10
    def add_credits(self):
        if self.__credits >= 0:
            self.__credits += 10
            self.__level = self._student_eval()
        else:
            print("Valeur de crédit incohérente")
    
    # Afficher les crédits
    def afficher_credits(self):
        print()
        print(f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits} points.")
        print()

    # Evaluation de l'élève
    def _student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif 90 > self.__credits >= 80:
            return "Très Bien"
        elif 80 > self.__credits >= 70:
            return "Bien"
        elif 70 > self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"
    
    # Informations de l'élève affichage
    def student_info(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("ID =", self.__numetud)
        print("Niveau =", self.__level)

# Initialisation d'un étudiant
student1 = Student("Doe", "John", 145)
# Ajout des crédits
for i in range (7):
    student1.add_credits()
student1.afficher_credits()

# Evaluation de l'élève
student1._student_eval()

# Informations de l'élève
student1.student_info()