class Temps:
    def __init__(self , Heures ,minutes ,secondes):
        self.Heures = Heures
        self.minutes = minutes
        self.secondes = secondes 

    def Ajouter_H(self):
        H = str(self.Heures) + 'H'
        return H
    
    def Ajouter_M(self):
        M = str(self.minutes) + 'M'
        return M   
    
    def Ajouter_S(self):
        s = str(self.secondes)+ 's'
        return s 
    
    def afficherTemps(self):
        return f'{self.Ajouter_H()}:{self.Ajouter_M()}:{self.Ajouter_S()}' 