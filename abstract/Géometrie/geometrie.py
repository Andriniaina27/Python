from abc import ABC, abstractmethod

class Geometrie(ABC):
    @abstractmethod
    def getSurface(self):
        pass

    def getPerimetre(self):
        pass