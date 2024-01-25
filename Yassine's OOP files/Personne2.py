from abc import ABCMeta , abstractmethod

class Personne (metaclass = ABCMeta):
    def __init__(self, code , nom , prenom , age):
        self._code = code 
        self._nom = nom 
        self._prenom = prenom
        self._age = age 


    def get_Code(self):
        return self._code
    
    def get_Nom(self):
        return self._nom
    
    def get_Prenom(self):
        return self._prenom
    
    def get_Age(self):
        return self._age

    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __eq__(self, per2) :
        pass


class employee(Personne):
    count = 0
    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        self.grade = grade
        employee.count += 1

    def get_grade(self):
        return self.grade

    
    def __str__(self):
        return f" {self._code} Eleve: {self._nom }  {self._prenom}, {self._age} ans  , grade {self.grade}"
    
    
    def __eq__(self, other):
        if self._code == other._code:
            return True
        else:
            return False
        
    
        
        
class Eleve(Personne):
    nbr = 0
    def __init__(self, code, nom, prenom, age, niveau , moyenne):
        super().__init__(code, nom, prenom, age)
        self.niveau = niveau
        self.moyenne = moyenne
        Eleve.nbr += 1


    def get_niveau(self):
        return self.niveau
    
    def get_moyenn(self):
        return self.moyenne

    
    def __str__(self):
        return f" {self._code} Eleve: {self._nom }  {self._prenom}, {self._age} ans  , Niveau :{self.niveau}, moy :{self.moyenne}"
    
    
    def __eq__(self, other):
        if self._code == other._code:
            return True
        else:
            return False
        

emp1 = employee("2","mazhare","yassine","20", "6th grade")
emp2 = employee("3","jean","tory","20", "7th grade")
emp3 = employee("4","patrik","clara","20", "3th grade")
print(emp2.__str__())
print(emp3.__eq__(emp2))
print(emp3.count)


eleve = Eleve("2","mazhare","yassine","20","3" ,"20")
eleve2 = Eleve("3","jean","tory","20","4", "12")
eleve3 = Eleve("4","patrik","clara","20","6", "17")
print(eleve.__str__())
print(eleve2.__eq__(eleve3))
print(eleve3.nbr)
