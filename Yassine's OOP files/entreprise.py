from abc import ABCMeta, abstractmethod

class Composition(metaclass=ABCMeta):
    def __init__(self, product=0, quantity=0):
        self.__product = product
        self.__quantity = quantity
    
    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self, value):
        self.__product = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

class Product(metaclass=ABCMeta):
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @abstractmethod
    def get_price_excluding_tax(self):
        pass

class BasicProduct(Product):
    def __init__(self, name, code, purchase_price):
        super().__init__(name, code) 
        self.__purchase_price = purchase_price

    def __str__(self):
        print(f"The name is: {self.name}, the code is: {self.code}")

    def get_price_excluding_tax(self):
        return self.__purchase_price

class CompositeProduct(Product):
    tax_rate = 0.18 

    def __init__(self, name, code, manufacturing_costs, constituent_list):
        super().__init__(name, code)
        self.__manufacturing_costs = manufacturing_costs
        self.__constituent_list =  constituent_list

    @property
    def manufacturing_costs(self):
        return self.__manufacturing_costs
    
    @manufacturing_costs.setter
    def manufacturing_costs(self, value):
        self.__manufacturing_costs = value

    @property
    def constituent_list(self):
        return self.__constituent_list
    
    @constituent_list.setter
    def constituent_list(self, value):
        self.__constituent_list = value

    def get_price_excluding_tax(self):
        return self.__manufacturing_costs

# Example Usage
COMPOSITE_PRODUCT1 = CompositeProduct("cake", "001", "20 dh", "4 eggs = 6 dh, 1L milk = 3.5 dh, 2 red apples = 1dh, 100g flour = 5dh")

print(COMPOSITE_PRODUCT1.name)
print(COMPOSITE_PRODUCT1.code)
print(COMPOSITE_PRODUCT1.constituent_list)
print(COMPOSITE_PRODUCT1.get_price_excluding_tax())
