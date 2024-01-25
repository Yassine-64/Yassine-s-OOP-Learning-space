

class Rectangle:

    def __init__(self, longueur, largeur):
        
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre(self):

        return 2 * (self.longueur + self.largeur)

    def aire(self):

        return self.longueur * self.largeur

    def IsCarre(self):

        return self.longueur == self.largeur

    def AfficherRectangle(self):

        print("longueur est:", self.longueur)
        print("largeur est:", self.largeur)
        print("perimetre est:", self.Perimetre())
        print("aire est:", self.aire())
        print("il s'agit d'un rectangle:", self.IsCarre())


