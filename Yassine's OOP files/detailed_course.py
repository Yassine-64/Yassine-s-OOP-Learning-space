# Python object-oriented programming
# Why we use OOP: Logically to group data and functions in a way that's easy to reuse and also easy to build upon if need be.

class Employee:
    # This is a method to show us the first, last name, and the email
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    # A second method to print the full name 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# The role of the constructor is to declare and build instances, also initialize the data members of the class
# A class is a type of personalized data or a frame to create instances from this frame

# Static is an attribute that is in relation with all instances of the class

# These are instances with attributes 
emp1 = Employee('yassine', 'mazhare', 4000)
emp2 = Employee('Test', 'User', 34399)

# Print email for each employee
print(emp1.email)
print(emp2.email)

# Let's show the full name manually for each employee and then we can use a method to do the same actions

# So now we created the method full name instead of printing it manually we can just do this 
print(emp1.fullname())
print(emp2.fullname())

# Comment on how to have two constructors in Python
# Default value DEV FOR NAME
# def __init__(self, nom="dev")

# Example of getters and setters
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

# Abstraction
# Abstract method declaration - a method that has no code, only the signature
# def sound(self)
# self

# Characteristics of abstract classes
# We cannot instantiate an abstract class (a class that has at least one abstract method)
# We can instantiate an abstract class if we have redefined the abstract methods

# Polymorphism:
# Polymorphism means you can use the same method or function name to perform similar actions on objects of different classes.
# This makes the code more flexible and allows treating objects in a general way without worrying about their specific type.

# Overriding:
# Method overriding occurs when you have a method in a parent class and the same method is redefined (implemented again) in a child class.
# This allows the child class to provide a specific implementation while retaining the same signature (name and parameters) as the method in the parent class.

# Abstract Method:
# An abstract method is a method declared in a class but has no concrete implementation at this location.
# It serves as a model or contract that derived classes must fulfill by providing a concrete implementation for this method.

# Example in Python:

# from abc import ABC, abstractmethod

# class Forme(ABC):
#     @abstractmethod
#     def calculer_surface(self):
#         pass

# In this example, Forme is an abstract class with an abstract method calculer_surface. Derived classes must implement this method.

# Interface:
# An interface is a class where all its methods are abstract.
# In Java, we cannot have multiple inheritance; we can only inherit from class A and implement class B, which is an interface.


