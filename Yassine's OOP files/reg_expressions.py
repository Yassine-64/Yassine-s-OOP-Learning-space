import re

A = '''
P1 est un produit compose de P2 et P3
P2 est produit elementaire 
P5 est un produit compose de P1 et P4
P4 est produit elementaire 
P9 est produit compose de P1, P6 et P4
P10 est un produit compose de P3 et P5
P11 est un produit compose de P5 et P3
'''
pattern = re.compile(r'(P\d+) (est produit elementaire)'A)
B = re.findall(r'(P\d+) (est produit elementaire)', A)
print(B)

C = re.findall(r"P\d est produit compose de (P\d), (P\d) et (P\d)", A)
print("Produit compose de trois produit ")
print(C)

D = re.findall(r'(P\d+) est un produit compose de (P3) et (P5)',A)
print("Produit composes de P3 et P5:")
print(D)

E = re.findall(r'(P\d+) est un produit compose de (?!P2)', A )
print("Produit composes sans P2:")
print(E)

F = re.findall(r'P9 est produit compose de (.+)', A)
print(F)