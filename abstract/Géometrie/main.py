from rectangle import Rectangle
from cercle import Cercle

longueur = float(input("Longueur : "))
largeur  = float(input("Largeur  : "))

rectangle = Rectangle(longueur, largeur)

print("...................")

rayon    = float(input("Rayon    : "))

cercle = Cercle(rayon)
print("...................")
rectangle.toString()
print("...................")
cercle.toString()