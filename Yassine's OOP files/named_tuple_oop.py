from collections import namedtuple , defaultdict , deque

description = namedtuple('description',['produit','detail'])

class Produit:
    def __init__(self, name):
        self.name = name
    
liste_des_produit = [Produit('P1'),Produit('P2'),Produit('P5'),Produit('P4'),Produit('P10')]

descriptions = [description(produit='P1' ,detail='p1 est un produit compose de P2 et P3'),
                description(produit='P2',detail='p2 est un produit elementaire'),
                description(produit='P5',detail='p5 est un produit compose de P1 et P4'),
                description(produit='P4',detail='p4 est un produit elementaire'),
                description(produit='P9',detail='p9 est un produit compose de P1 et P6 et P4')]

#had methode pour convertir les description into a dict {-asdict() method provided b named tuple    
description_dicts =[desc._asdict() for desc in descriptions]   
# ncreer liste description un objet de type default dict fih ga3 les desc dial produit   
ListeDescription = defaultdict(list)   
for desc in description_dicts:
    ListeDescription[desc['produit']].append(desc['detail'])


DeqDescription = deque()
for detail in ListeDescription.values():
    DeqDescription.extend(detail)


