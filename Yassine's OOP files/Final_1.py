class Salarié:
    nombre_instance = 0
    matricule = 0

    def __init__(self, nom, sociale, etat_civile, adresse, salaire):
        self._nom = nom
        self._sociale = sociale
        self._etat_civile = etat_civile
        self._adresse = adresse
        self._salaire = salaire
        Salarié.nombre_instance += 1
        Salarié.matricule += 1

    def __eq__(self, other):
        return isinstance(other, Salarié) and self._matricule == other._matricule

    def __str__(self):
        return f"Nom: {self._nom}, Matricule: {self._matricule}, Salaire: {self._salaire}"
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def sociale(self):
        return self._sociale

    @sociale.setter
    def sociale(self, value):
        self._sociale = value

    @property
    def etat_civile(self):
        return self._etat_civile

    @etat_civile.setter
    def etat_civile(self, value):
        self._etat_civile = value

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, value):
        self._salaire = value



class Patron(Salarié):
    count = 0

    def __init__(self, nom, sociale, etat_civile, adresse, salaire, prime_de_risque=0):
        super().__init__(nom, sociale, etat_civile, adresse, salaire)
        self._prime_de_risque = prime_de_risque
        Patron.count += 1

    def __eq__(self, other):
        return isinstance(other, Patron) and super().__eq__(other) and \
            self._salaire + self._prime_de_risque == other._salaire + other._prime_de_risque

    def __str__(self):
        return super().__str__() + f", Prime de risque: {self._prime_de_risque}"
    
    @property
    def prime_de_risque(self):
        return self._prime_de_risque

    @prime_de_risque.setter
    def prime_de_risque(self, value):
        self._prime_de_risque = value



class Vendeur(Salarié):
    count2 = 0

    def __init__(self, nom, sociale, etat_civile, adresse, numero_sec, salaire, commission=0):
        super().__init__(nom, sociale, etat_civile, adresse, numero_sec, salaire)
        self._commission = commission
        Vendeur.count2 += 1

    def __eq__(self, other):
        return isinstance(other, Vendeur) and super().__eq__(other) and \
            self._salaire + self._commission == other._salaire + other._commission

    def __str__(self):
        return super().__str__() + f", Commission: {self._commission}"


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



p = Patron("yassine", "dddd", "dvs", "jbfcqkebf", 1378, 30000, 1000)
p1 = Patron("bingoo", "dddd", "dvs", "jbfcqkebf", 1378, 30000, 1000)

print(p1.__eq__(p))
print(p)
