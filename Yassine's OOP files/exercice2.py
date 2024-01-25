from abc import ABCMeta , abstractmethod 
class Animal (metaclass = ABCMeta):
    def __init__(self , name, age, race ):
        self.name = name
        self.age = age 
        self.race = race

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    @property

    def sound(self):
        return "woof woof"
    
    @property
    def move(self):
        return "t7rk "
    
class Bird(Animal):

    @property 
    def sound(self):
        return "ZZZZTZTZTZTZT"
    
    @property 
    def move(self):
        return "ZZZZTZTZTZTZT"
    

peruche = Bird("nico","19","Peruche")

print(peruche.sound)
print(peruche.move)

