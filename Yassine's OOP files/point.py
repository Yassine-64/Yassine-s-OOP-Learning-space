class Point:
    def __init__(self, abscisse=0, ordonnee=0):
        self._abscisse = abscisse
        self._ordonnee = ordonnee

    @property
    def abscisse(self):
        return self._abscisse
    
    @abscisse.setter
    def abscisse(self, valeur):
        self._abscisse = valeur

    @property
    def ordonnee(self):
        return self._ordonnee
    
    @ordonnee.setter
    def ordonnee(self, valeur):
        self._ordonnee = valeur

    def __str__(self):
        return f"({self.abscisse},{self.ordonnee})"

    def __eq__(self, other):
        return self.abscisse == other.abscisse and self.ordonnee == other.ordonnee

    
    def calculer_distance(self, other):
        return ((self.abscisse - other.abscisse)**2 + (self.ordonnee - other.ordonnee)**2)**0.5

    def calculer_milieu(self, other):
        xM = (self.abscisse + other.abscisse) / 2
        yM = (self.ordonnee + other.ordonnee) / 2
        return Point(xM, yM)

class TroisPoints:
    def __init__(self, point1, point2, point3):
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3

    @property
    def get_point1(self):
        return self._point1
    
    @point1.setter
    def point1(self, valeur):
        self._point1 = valeur

    @property
    def get_point2(self):
        return self._point2
    
    @point2.setter
    def point2(self, valeur):
        self._point2 = valeur

    @property
    def get_point3(self):
        return self._point3
    
    @point3.setter
    def point3(self, valeur):
        self._point3 = valeur

    def sont_alignes(self):
        distance12 = self.point1.calculer_distance(self.point2)
        distance13 = self.point1.calculer_distance(self.point3)
        distance23 = self.point2.calculer_distance(self.point3)

        return (
            distance12 == distance13 + distance23 or
            distance13 == distance12 + distance23 or
            distance23 == distance12 + distance13
        )

    def est_isocèle(self):
        distance12 = self.point1.calculer_distance(self.point2)
        distance13 = self.point1.calculer_distance(self.point3)
        distance23 = self.point2.calculer_distance(self.point3)

        return (
            distance12 == distance13 or
            distance12 == distance23 or
            distance23 == distance13
        )


point1 = Point(4, 3)
point2 = Point(0, 0)
point3 = Point(8, 6)

triangle = TroisPoints(point1, point2, point3)
print(triangle.sont_alignes())  
print(triangle.est_isocèle())   
