from geometrie import Geometrie
import math

class Cercle(Geometrie):
    def __init__(self, rayon):
        self.rayon = rayon

    def __str__(self):
        return self.rayon
    
    def getSurface(self):
        return pow(self.rayon, 2) * math.pi
    
    def getPerimetre(self):
        return (self.rayon * 2) * math.pi
    
    def toString(self):
        output = print(f"Cercle :")
        output = print(f"Surface   = {self.getSurface()}")
        output = print(f"Perimetre = {self.getPerimetre()}")
        return output
