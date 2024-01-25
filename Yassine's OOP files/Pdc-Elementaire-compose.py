from collections import namedtuple , defaultdict , deque
from abc import ABCMeta, abstractmethod

from abc import ABCMeta, abstractmethod

class Composition:
    def __init__(self, product=None, quantity=0):
        self.product = product
        self.quantity = quantity
    
    def __eq__(self, other):
        if isinstance(other, Composition):
            return self.product == other.product and self.quantity == other.quantity
        return False

class Product(metaclass=ABCMeta):
    def __init__(self, name, code):
        self._name = name
        self._code = code

    @property
    def name(self):
        return self._name
    
    @property
    def code(self):
        return self._code

    @abstractmethod
    def get_prix_HT(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.code == other.code
        return False
    
class ProduitElementaire(Product):
    def __init__(self, name, code, prixAchat):
        super().__init__(name, code)
        self._prixAchat = prixAchat

    @property
    def prixAchat(self):
        return self._prixAchat
    
    @prixAchat.setter
    def prixAchat(self, value):
        self._prixAchat = value

    def __str__(self):
        return f"ProduitElementaire: Nom - {self.name}, Code - {self.code}, Prix d'Achat - {self.prixAchat}"

    def get_prix_HT(self):
        return self.prixAchat

class ProduitCompose(Product):
    tauxTVA = 0.18

    def __init__(self, name, code, fraisFabrication):
        super().__init__(name, code)
        self._fraisFabrication = fraisFabrication
        self._listeConstituants = []

    @property
    def fraisFabrication(self):
        return self._fraisFabrication
    
    @fraisFabrication.setter
    def fraisFabrication(self, value):
        self._fraisFabrication = value

    @property
    def listeConstituants(self):
        return self._listeConstituants

    def add_constituant(self, composition):
        self._listeConstituants.append(composition)

    def remove_constituant(self, composition):
        self._listeConstituants.remove(composition)

    def clear_constituants(self):
        self._listeConstituants.clear()

    def __str__(self):
        return f"ProduitCompose: Nom - {self.name}, Code - {self.code}, Frais de Fabrication - {self.fraisFabrication}"
    
    def get_prix_HT(self):
        total_price_ht = 0

        for composition in self.listeConstituants:
            total_price_ht += composition.product.get_prix_HT() * composition.quantity

        return total_price_ht + self.fraisFabrication


        


elementaire1 = ProduitElementaire("Elem1", "E1", 10)
elementaire2 = ProduitElementaire("Elem2", "E2", 15)

compose1 = ProduitCompose("Compose1", "C1", 5)
compose1.listeConstituants.append(Composition(elementaire1, 2))
compose1.listeConstituants.append(Composition(elementaire2, 3))

elemen_codes = compose1.get_elementaire_product_codes()
print(f"le code de  Compose1: {elemen_codes}")

total_price_ht_compose1 = compose1.get_prix_HT()
print(f"Total Price HT for Compose1: {total_price_ht_compose1}")   



ListeProduit = [elementaire1, elementaire2, compose1]

# hadi named tuple fiha desc o prduct detail
Description = namedtuple('Description', ['Produit', 'Détail'])

# creena default dict bach nstockiw les description 
ListeDescription = defaultdict(list)

# Creena deque bach nstockiw  Description objects
DeqDescription = deque()

# Boucle bach nchoufo chaque produit f la list 
for produit in ListeProduit:
    # Vérifiez si le produit mn type produit elementaire 
    if isinstance(produit, ProduitElementaire):
        # Creer wahd description l produit elementaire 
        detail = f"{produit.name} est un produit Élémentaire"
    # condition ila kan produit de type produit composer
    elif isinstance(produit, ProduitCompose):
        # hado les nom des constituant et zdna 3lihom "et"
        constituants = " et ".join([comp.product.name for comp in produit.listeConstituants])
        # description pour produit composer
        detail = f"{produit.name} est composé de {constituants}"

    # creena wahd objet de type descr avec le nom et description dilana
    desc = Description(produit.name, detail)

    # nzido l'objet Description l dik la liste associée au nom dial produit  f  ListeDescription
    ListeDescription[produit.name].append(desc)

    # Convertissez l'objet Description l wahd dictionnaire ou nzidoh à DeqDescription
    DeqDescription.append(dict(desc._asdict()))


print("ListeDescription:")
for key, value in ListeDescription.items():
    print(f"{key}: {value}")

print("DeqDescription:")
for desc_dict in DeqDescription:
    print(desc_dict)


