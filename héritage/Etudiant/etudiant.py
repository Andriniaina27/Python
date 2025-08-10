from personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, filiere):
        super().__init__(nom, age)
        self.filiere = filiere

    def info(self):
        print(f"Je suis étudiant en {self.filiere}")

