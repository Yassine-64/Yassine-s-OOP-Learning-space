#Python object oriented programming
#why we use oop  : logically to group data and functions in a way that's easy to reuse and also easy to build upon if need be 


class Employee:
    #this is a  method to sho us the first , last name and the email
    def __init__(self, first ,last ,pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    #a second method to print the full name 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #
#le role de constructeur et de declarer et construire des instance aussi initialiser les donne membre de classe 
#class est un type de donnnée personnaliser   ou bien frame pour y cree des instances a partir de ce frame 

#static est un attribut:
#  qui est en relation avec tous les instances de la classe 

#these are instance has attributs 
emp1 = Employee('yassine','mazhare',4000)
emp2 = Employee('Test','User',34399)

# print(emp1)
# print(emp2)
# #every instance has a attribut specific or values 
# emp1.first = "yassine"
# emp1.last = "mazhare"
# emp1.email = "yassine.mazhare@gmail.com"
# emp1.pay = 4000

# emp2.first = "Test"
# emp2.last = "User"
# emp2.email = "Test.User@gmail.com"
# emp2.pay = 34399
#import copy
# stg2 = copy.copy(stg1)

print(emp1.email)
print(emp2.email)

#let's show the full name manually for each employee and then we can use a method to do the same actions 

# print('{} {}'.format(emp1.first, emp1.last))

#so now we created the method full name instead of printing it manually we can just do this 
print(emp1.fullname())
print(emp2.fullname())

# comment mettre deux constructeur en python 

# valeur par defaut DEV POUR LE NOM
#def__init__(self,nom="dev")



def get_longueur(self):
        return self.longueur

def set_longueur(self, value):
        self.longueur = value

def get_largeur(self):
        return self.largeur

def set_largeur(self, value):
        self.largeur = value 

def get_code(self):
        return self.code

def IsCarre(self):

        return self.longueur == self.largeur

#abstraction 

#@abstractmethod
# declarina methode khawya   methode qui n a pas de code on ecrit juste la signature  
#def sound(self)
#self

# caracteristique de classe abstraite
# on ne peut pas instancier dune classe abstraite (une classe qui a une seule methode abstraite )

#on peut instancier dune classe abstraite si on a redefini les methode abstraite 

# from abc import ABCMeta , abstract method 
#class name (metaclass = ABCMeta)
#Polymorphisme :

# Le polymorphisme signifie que vous pouvez utiliser le même nom de méthode ou de fonction pour effectuer des actions similaires sur des objets de différentes classes. Cela rend le code plus flexible et permet de traiter des objets de manière générale sans se soucier de leur type spécifique.

# lencapsulation est un principe qui nous permet de fermer acces aux attribut en mettant dok les att prives o tan accediw lihom b getters o la bghina n controliw o nmodifiw tandiro setters
#polymorphisme taykon 3ndna resultat differe selon les types de donnes et parametre 
# Abstraction :

# L'abstraction consiste à simplifier un système complexe en isolant les aspects essentiels et en ignorant les détails non pertinents. En programmation, c'est comme créer une interface simple pour interagir avec un objet sans se soucier de sa complexité interne.

# Caractéristiques de l'abstraction : 

#     Identification des Caractéristiques Essentielles : Isoler les aspects importants.
#     Création de Modèles : Utiliser des classes ou des interfaces comme modèles.
#     Masquage des Détails : Cacher les détails complexes de l'implémentation.

# Différence entre Polymorphisme et Abstraction :

#     Polymorphisme : Se rapporte à l'utilisation du même nom de méthode sur des objets de différentes classes.
#     Abstraction : Se rapporte à la simplification d'un système en isolant les aspects essentiels.

# Surcharge (Overriding) :

# La surcharge de méthode (ou overriding) se produit lorsque vous avez une méthode dans une classe parente et que la même méthode est redéfinie (implémentée à nouveau) dans une classe enfant. Cela permet à la classe enfant de fournir une implémentation spécifique tout en conservant la même signature (nom et paramètres) que la méthode de la classe parente.


# Méthode Abstraite :

# Une méthode abstraite est une méthode déclarée dans une classe, mais qui n'a pas d'implémentation concrète à cet endroit. Elle sert de modèle ou de contrat que les classes dérivées doivent remplir en fournissant une implémentation concrète pour cette méthode.

# Caractéristiques de la méthode abstraite :

#     Déclaration sans Implémentation : La méthode est déclarée dans la classe, mais sans code à l'intérieur.
#     Obligation d'Implémentation : Toute classe dérivée doit fournir une implémentation pour toutes les méthodes abstraites de sa classe parente.
#     Utilisation de la Classe Abstraite : Une classe avec au moins une méthode abstraite doit être déclarée abstraite,et elle ne peut pas être instanciée directement. 

# Exemple en Python :

# python

# from abc import ABC, abstractmethod

# class Forme(ABC):
#     @abstractmethod
#     def calculer_surface(self):
#         pass     

# Dans cet exemple, Forme est une classe abstraite avec une méthode abstraite calculer_surface. Les classes dérivées doivent implémenter cette méthode.



#interface c'est une classe que tout ses methode sont abstraite 
#f java on ne peut pas faire un heritage multiple , on peut juste heriter d une classe A et implementer d une classe b qui est interfaces  


