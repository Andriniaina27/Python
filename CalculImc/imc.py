class Imc(object):
    def __init__(self,p ,t):
        self.poids  = p
        self.taille = t

    def getPoids(self):
        return print(f"Poids  : {self.poids}")
    
    def getTaille(self):
        return print(f"Taille : {self.taille}")

    def calculImc(self):
        imc = self.poids / pow(self.taille, 2)
        return imc
    
    def getStatus(status):
        if status.calculImc() < 18:
            mess = "Vous êtes maigre"
        elif 18.5 < status.calculImc() and status.calculImc() < 25:
            mess = "C'est normal"
        elif 25.5 < status.calculImc() and status.calculImc() < 30:
            mess = "Surpoids"
        elif 30.5 < status.calculImc() and status.calculImc() < 40:
            mess = "Obèse modéré"
        else:
            mess = "Obèse sévère"
        return mess

# def addImc():
poids = int(input("Poids   : "))
taille = float(input("Taille : "))
imc = Imc(poids, taille)

print("..........................................")
print(f"Poids  : {imc.poids} \nTaille : {imc.taille} \nCalcul : {imc.calculImc()}\nObservation : {imc.getStatus()}")