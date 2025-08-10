class Eau:
    def __init__(self, nom, poids):
        self.nom = nom
        self.poids = poids

    def __str__(self):
        chaine = self.nom
        chaine = self.poids
        return chaine
    
    def calculEau(self):
        calcul = ((self.poids - 20)*15)+1500
        return float(calcul)
    
    def getStatus(self):
        print(f"{self.nom} aura besoin chaque jour de {self.calculEau()}")