from geometrie import Geometrie
class Rectangle(Geometrie):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        rec = self.longueur
        rec = self.largeur
        return rec
    
    def getSurface(self):
        surface = self.longueur * self.largeur
        return float(surface)
    
    def getPerimetre(self):
        perimetre = (self.longueur + self.largeur) * 2
        return float(perimetre)
    
    def toString(self):
        output = print(f"Rectangle : ")
        output = print(f"Surface   = {self.getSurface()}")
        output = print(f"Perimetre = {self.getPerimetre()}")
        return output