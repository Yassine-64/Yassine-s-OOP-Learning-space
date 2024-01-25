from abc import ABC, abstractmethod
import random

class Entreprise(ABC):
    def __init__(self, nom, num_securite, etat_civile, adresse):
        self.__nom = nom
        self.__num_securite = num_securite
        self.__etat_civile = etat_civile
        self.__adresse = adresse
        self.salaire = 0
        self.__matricule = random.randint(0, 100)

    @property
    def getNom(self):
        return self.__nom
    
    def setNom(self, value):
        self.__nom = value

    @property
    def getNum(self):
        return self.__num_securite

    def setNum(self, value):
        self.__num_securite = value

    @property
    def getEtat(self):
        return self.__etat_civile

    def setEtat(self, value):
        self.__etat_civile = value

    @property
    def getAdresse(self):
        return self.__adresse

    def setAdresse(self, value):
        self.__adresse = value

    @property
    def getMatricule(self):
        return self.__matricule

    @abstractmethod
    def __str__(self):
        pass
    
    def __eq__(self, other):
        return isinstance(other, Entreprise) and self.__matricule == other.__matricule

class Patron(Entreprise):
    num_patron = 0

    def __init__(self, nom, num_securite, etat_civile, adresse, prim_risque):
        super().__init__(nom, num_securite, etat_civile, adresse)
        self.__prim_risque = prim_risque
        Patron.num_patron += 1
        self.salaire = 15000

    @property
    def getPrime(self):
        return self.__prim_risque
    
    def setPrim(self, value):
        self.__prim_risque = value 

    def __str__(self):
        return f"""Nom:{self.getNom}
Matricule:{self.getMatricule}
Numero de securite social:{self.getNum}
Etat civile :{self.getEtat}
Salaire:{self.salaire + self.__prim_risque} DH
Adresse: {self.getAdresse}
"""

    def __eq__(self, other):
        return isinstance(other, Patron) and super().__eq__(other) and self.salaire == other.salaire

class Vendeur(Entreprise):
    num_vendeur = 0

    def __init__(self, nom, num_securite, etat_civile, adresse, commissio):
        super().__init__(nom, num_securite, etat_civile, adresse) 
        self.__commissio = commissio
        self.salaire = 11000
        Vendeur.num_vendeur += 1
    
    @property
    def getCommmision(self):
        return self.__commissio

    def __str__(self):
        return f"""Nom: {self.getNom}
Numero de securite social: {self.getNum}
Etat civile: {self.getEtat}
Salaire: {self.salaire + self.__commissio} DH
Adresse: {self.getAdresse}
"""

    def __eq__(self, other):
        return isinstance(other, Vendeur) and super().__eq__(other) and self.salaire == other.salaire

class Caisier(Entreprise):
    num_caisier = 0

    def __init__(self, nom, num_securite, etat_civile, adresse):
        super().__init__(nom, num_securite, etat_civile, adresse)
        self.salaire = 3000
        Caisier.num_caisier += 1

    def __str__(self):
        return f"""Nom: {self.getNom}
Numero de securite social: {self.getNum}
Etat civile: {self.getEtat}
Salaire: {self.salaire} DH
Adresse: {self.getAdresse}
"""

    def __eq__(self, other):
        return isinstance(other, Caisier) and self.salaire == other.salaire


patron = Patron("simo nachit", 123, "Celebataire", "LosAngles num: 1234", 1300)
patron2 = Patron("hannane rexona", 111, "puta", "Douar Iziki num:28", 900)

print(patron)
print(patron2)
print("nombre de patron est :", Patron.num_patron)
print(patron.__eq__(patron2))

caisier = Caisier("Amin chawlin", 333, "mniyok", "Amezmiz num: 22")
caisier2 = Caisier("Salma terma", 23, "mniyoka", "Marrekch num: 2")

print(caisier)
print(caisier2)
print("nombre de caisier dans l'entreprise est:", Caisier.num_caisier)
print(caisier.__eq__(caisier2))
