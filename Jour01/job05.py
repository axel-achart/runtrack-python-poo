class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"x : {self.x}, y : {self.y}")
    
    def afficherX(self):
        print(f"x : {self.x}")
    
    def afficherY(self):
        print(f"y : {self.y}")

    def changerX(self):
        self.x = 50
    
    def changerY(self):
        self.y = 50

mon_point = Point(0, 0)

mon_point.afficherLesPoints()
mon_point.afficherX()
mon_point.afficherY()
mon_point.changerX()
mon_point.changerY()
mon_point.afficherLesPoints()