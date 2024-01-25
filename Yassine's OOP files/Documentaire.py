class Documentaire:
    n_objet = 0

    def __init__(self,titre,Date,) :
        Documentaire.n_objet +=1 
        self.code = Documentaire.n_objet
        self.titre = titre
        self.Date = Date 
        

    def get_titre(self):
        return self.titre
    
    def set_titre(self, value):
        self.titre = value

    def get_Date(self):
        return self.Date
    
    def set_Date(self, value):
        self.Date = value 

    def get_code(self):
        return self.code
    
    def Tostring(self):
        return f"Documentaire : titre={self.titre} Date ={self.Date} code={self.code}"
    
    def Equals(self,other):
        return self.code == other.get_code() 
    

class Exemplaire(Documentaire):
    def __init__(self, titre , Date, numero ,date_achat):
        super().__init__(titre, Date)
        self.numero = numero
        self.date_achat = date_achat

    def get_numero(self):
        return self.numero
    
    def set_numero(self,value):
        self.numero = value 

    def get_date_achat(self):
        return self.date_achat
    
    def set_date_achat(self,value):
        self.date_achat = value

    def Tostring(self):
        return f"{super().Tostring()}, numero ={self.numero}, date d'achat={self.date_achat}"
    
    def Equals(self, other):
        return isinstance(other,Exemplaire) and self.numero == other.get_numero
    

Doc1 = Documentaire('YASSINE','22-12-2023')
exemp1 = Exemplaire('nachit','01-1-2024','0004', '4-07-2024')


print(f"le nombre d'objet est : {Documentaire.n_objet}")
print(Doc1.Tostring())
print(exemp1.Tostring())



