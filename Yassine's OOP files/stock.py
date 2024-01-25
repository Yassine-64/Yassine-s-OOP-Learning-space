class Produit:
    n_produit = 0

    def __init__(self, reference, designation, prix_achat, prix_vente):
        Produit.n_produit += 1
        self.reference = reference
        self.designation = designation
        self._prix_achat = prix_achat
        self._prix_vente = prix_vente
        self._nbr_exemplaire = 0  

    @property
    def nbr_exemplaire(self):
        return self._nbr_exemplaire

    @nbr_exemplaire.setter
    def nbr_exemplaire(self, value):
        self._nbr_exemplaire = value

    @property
    def prix_achat(self):
        return self._prix_achat

    @prix_achat.setter
    def prix_achat(self, value):
        self._prix_achat = value

    @property
    def prix_vente(self):
        return self._prix_vente

    @prix_vente.setter
    def prix_vente(self, value):
        self._prix_vente = value

    def __str__(self):
        return f"Produit: Référence={self.reference} Prix d'achat={self.prix_achat} Vente={self.prix_vente} Designation={self.designation}"

    def __eq__(self, other):
        if isinstance(other, Produit):
            return self.reference == other.reference
        return False

    def augmenter(self, quantite):
        self.nbr_exemplaire += quantite

    def diminuer(self, quantite):
        self.nbr_exemplaire -= quantite


class Commande:
    def __init__(self, produit, date, quantite):  # Corrected method name
        self.produit = produit
        self.date = date
        self.quantite = quantite

    @property
    def get_date(self):
        return self.date

    @property
    def get_quantite(self):
        return self.quantite

    def set_date(self, value):  
        self.date = value

    def set_quantite(self, value): 
        self.quantite = value

    def __str__(self):
        return f"Commande: Produit={self.produit.__str__()} Date={self.date} Quantité={self.quantite}"



prd1 = Produit("798725", "jegkqjgn", 100, 5001)
prd2 = Produit("998898", "fjqmfl", 2000, 53476)
prd3 = Produit("8278720", "kjqfm", 2001, 2789)
com1 = Commande(prd1, "8/9/2018", 777)
com2 = Commande(prd2, "9/3/1999", 455)

print(Produit.n_produit)
print(prd1.__str__())
print(prd2.__str__())
print(prd3.__str__())
print(prd1.__eq__(prd2))
print(prd2.__eq__(prd3))
print(com1.__str__())
print(com2.__str__())



# for key, value in dictionnnaire dialna.items():
# print(key,value)



