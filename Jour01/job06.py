class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self, prenom):
        self.prenom = prenom


singe = Animal()
print(f"L'age de l'animal {singe.age} ans")


singe.vieillir()
print(f"L'age de l'animal {singe.age} ans")


singe.nommer("Singe Européen")
print(f"L'animal se nomme {singe.prenom}")