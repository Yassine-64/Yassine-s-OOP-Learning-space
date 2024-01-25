class Produit:

    def __init__(self, nom, prix_achat, prix_vente, description="Pas de description"):
        self.nom = nom
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock = 0
        self.description = description

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def prix_achat(self):
        return self._prix_achat

    @prix_achat.setter
    def prix_achat(self, nouveau_prix_achat):
        self._prix_achat = nouveau_prix_achat

    @property
    def prix_vente(self):
        return self._prix_vente

    @prix_vente.setter
    def prix_vente(self, nouveau_prix_vente):
        self._prix_vente = nouveau_prix_vente

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nouveau_stock):
        self._stock = nouveau_stock

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, nouvelle_description):
        self._description = nouvelle_description

    def afficher_description(self):
        print(f"Description du produit {self.nom}: {self.description}")

    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description

    def augmenter_stock(self, quantite):
        self.stock += quantite

    def diminuer_stock(self, quantite):
        if self.stock >= quantite:
            self.stock -= quantite
        else:
            print(f"Stock insuffisant pour {self.nom}")

    def __str__(self):
        return f"Nom: {self.nom}\nPrix d'achat: {self.prix_achat}\nPrix de vente: {self.prix_vente}\nStock: {self.stock}\nDescription: {self.description}"

        


class Magasin:
    def __init__(self, adresse):
        self.adresse = adresse
        self.stock_produits = []

    def ajouter_produit(self, produit):
        self.stock_produits.append(produit)

    def acheter_produit(self, reference_produit, nombre_exemplaires):
        self.stock_produits[reference_produit].augmenter_stock(nombre_exemplaires)

    def vendre_produit(self, reference_produit, nombre_exemplaires):
        self.stock_produits[reference_produit].diminuer_stock(nombre_exemplaires)

    def bilan(self):
        for produit in self.stock_produits:
            print(produit.obtenir_valeurs())

    def ajouter_livre(self, livre):
        self.stock_produits.append(livre)

    def ajouter_cd(self, cd):
        self.stock_produits.append(cd)

    def rechercher_produit(self, nom):
        for produit in self.stock_produits:
            if produit.nom == nom:
                return produit
        return None

    def rechercher_produit_par_mot(self, mot):
        resultats = []
        for produit in self.stock_produits:
            if mot in produit.description:
                resultats.append(produit)
        return resultats


class Livre(Produit):
    def __init__(self, nom, prix_achat, prix_vente, auteur, editeur, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self._auteur = auteur
        self._editeur = editeur

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, nouveau_editeur):
        self._editeur = nouveau_editeur


class Cd(Produit):
    def __init__(self, nom, prix_achat, prix_vente, auteur, interprete, titres, description="Pas de description"):
        super().__init__(nom, prix_achat, prix_vente, description)
        self._auteur = auteur
        self._interprete = interprete
        self._titres = titres

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, nouveau_interprete):
        self._interprete = nouveau_interprete

    @property
    def titres(self):
        return self._titres

    @titres.setter
    def titres(self, nouveaux_titres):
        self._titres = nouveaux_titres
