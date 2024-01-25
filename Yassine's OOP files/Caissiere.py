class Caissiere(Salarié):
    count3 = 0

    def __init__(self, nom, sociale, etat_civile, adresse, numero_sec, salaire):
        super().__init__(nom, etat_civile, adresse, numero_sec, salaire)
        Caissiere.count3 += 1

    def __eq__(self, other):
        return isinstance(other, Caissiere) and super().__eq__(other) and self._salaire == other._salaire

    def __str__(self):
        return super().__str__()
    
    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, value):
        self._salaire = value