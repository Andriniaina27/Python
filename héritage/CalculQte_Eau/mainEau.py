from eau import Eau

nom = input("Nom   : ")
poids = int(input("Poids : "))
eau = Eau(nom, poids)
print("....................")
eau.getStatus()