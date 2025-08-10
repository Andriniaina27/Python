from datetime import datetime,timedelta

class Employe:
    def __init__(self, matricule, nom, prenom, dateN, dateE, salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.dateN = dateN
        self.dateE = dateE
        self.salaire = salaire

    def __str__(self):
        chaine = print(f"Matricule         : {self.matricule}")
        chaine = print(f"Nom               : {self.nom}")
        chaine = print(f"Prénom            : {self.prenom}") 
        chaine = print(f"Date de naissance : {self.dateN}")
        chaine = print(f"Date d'embauche   : {self.dateE}")
        chaine = print(f"Salaire de base   : {self.salaire}")
        return chaine
    
    def Age(self):
        dateN = datetime.strptime(self.dateN, "%d/%m/%Y")
        dateJ = datetime.today()
        annees = dateJ.year - dateN.year
        return annees
    
    def Anciennete(self):
        dateE = datetime.strptime(self.dateE, "%d/%m/%Y")
        dateJ = datetime.now()
        annees = dateJ.year - dateE.year
        return annees

    def augmentationSalaire(self):
        if self.Anciennete() < 5:
            salaire = self.salaire + (self.salaire * 2) / 100
        elif self.Anciennete() < 10:
            salaire = self.salaire + (self.salaire * 5) / 100
        else:
            salaire = self.salaire + (self.salaire * 10) / 100
        return int(salaire)

matricule = input("Matricule                : ")
nom       = input("Nom                           : ")
prenom    = input("Prenom                        : ")
dateN     = input("Date de naissance (dd/mm/YYY) : ")
dateE     = input("Date d'embauche (dd/mm/YYY)   : ")
salaire   = int(input("Salaire                       : "))
employe = Employe(matricule, nom, prenom, dateN, dateE, salaire)

print("......................................")
print(f"Matricule   : {employe.matricule}")
print(f"Nom complet : {employe.nom} {employe.prenom}")
print(f"Age         : {employe.Age()} ans")
print(f"Ancienneté  : {employe.Anciennete()} an(s)")
# print(f"Salaire     : {employe.augmentationSalaire()} Ariary")
