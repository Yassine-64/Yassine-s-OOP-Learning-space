import random
import csv

class CompteBancaire:
    def __init__(self, identifiant_client, solde=0):
        self.identifiant_client = identifiant_client
        self.numero_compte = int(str(identifiant_client) + str(random.randint(0, 100)))
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} unités. Nouveau solde : {self.solde}")

    def retirer(self, montant):
        if montant > self.solde:
            print("Fonds insuffisants !")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} unités. Nouveau solde : {self.solde}")

    def afficher_infos(self):
        print(f"Identifiant client : {self.identifiant_client}, Numéro de compte : {self.numero_compte}, Solde : {self.solde}")

class Banque:
    def __init__(self):
        self.comptes = {}
        self.secret_clients = {}
        self.client_compte = {}

    def ajouter_compte(self, identifiant_client):
        if identifiant_client not in self.comptes:
            nouveau_compte = CompteBancaire(identifiant_client)
            self.comptes[identifiant_client] = nouveau_compte
            secret = input(f"Définir un code secret pour le client {identifiant_client} : ")
            self.secret_clients[identifiant_client] = secret
            self.client_compte[identifiant_client] = nouveau_compte.numero_compte
            print(f"Compte créé avec succès pour le client {identifiant_client}.")
        else:
            print(f"Compte existant déjà pour le client {identifiant_client}.")

    def supprimer_compte(self, identifiant_client):
        if identifiant_client in self.comptes:
            del self.comptes[identifiant_client]
            del self.secret_clients[identifiant_client]
            del self.client_compte[identifiant_client]
            print(f"Compte supprimé avec succès pour le client {identifiant_client}.")
        else:
            print(f"Aucun compte trouvé pour le client {identifiant_client}.")

    def afficher_comptes(self):
        for compte in self.comptes.values():
            compte.afficher_infos()

    def menu_client(self, identifiant_client):
        while True:
            print("\nMenu Client :")
            print("1. Modifier le mot de passe")
            print("2. Afficher le solde")
            print("3. Déposer de l'argent")
            print("4. Retirer de l'argent")
            print("5. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == '1':
                nouveau_mot_de_passe = input("Entrez un nouveau mot de passe : ")
                self.secret_clients[identifiant_client] = nouveau_mot_de_passe
                print("Mot de passe modifié avec succès.")

            elif choix == '2':
                numero_compte = self.client_compte[identifiant_client]
                print(f"Votre solde est : {self.comptes[identifiant_client].solde}")

            elif choix == '3':
                montant = float(input("Entrez le montant à déposer : "))
                self.comptes[identifiant_client].deposer(montant)

            elif choix == '4':
                montant = float(input("Entrez le montant à retirer : "))
                self.comptes[identifiant_client].retirer(montant)

            elif choix == '5':
                print("Sortie du menu client. Au revoir !")
                break

            else:
                print("Choix invalide. Veuillez entrer une option valide.")

    def ajouter_client(self, num_cl, mdp_client, num_c, solde_c):
        self.secret_clients[num_cl] = mdp_client
        self.comptes[num_cl] = CompteBancaire(num_cl, solde_c)
        self.client_compte[num_cl] = num_c

    def supprimer_client(self, num_c):
        if num_c in self.comptes:
            del self.comptes[num_c]
            for client, compte in self.client_compte.items():
                if compte == num_c:
                    del self.secret_clients[client]
                    del self.client_compte[client]
                    break
            print(f"Client avec compte {num_c} supprimé avec succès.")
        else:
            print(f"Aucun compte trouvé avec le numéro {num_c}.")

def modifier_mot_de_passe_client(banque, identifiant_client, nouveau_mot_de_passe):
    if identifiant_client in banque.secret_clients:
        banque.secret_clients[identifiant_client] = nouveau_mot_de_passe
        print("Mot de passe modifié avec succès.")
    else:
        print(f"Client {identifiant_client} non trouvé.")

def deposer_argent(banque, identifiant_client, montant):
    if identifiant_client in banque.client_compte:
        numero_compte = banque.client_compte[identifiant_client]
        if numero_compte in banque.comptes:
            banque.comptes[numero_compte].deposer(montant)
        else:
            print(f"Compte {numero_compte} non trouvé.")
    else:
        print(f"Client {identifiant_client} non trouvé.")

def retirer_argent(banque, identifiant_client, montant):
    if identifiant_client in banque.client_compte:
        numero_compte = banque.client_compte[identifiant_client]
        if numero_compte in banque.comptes:
            banque.comptes[numero_compte].retirer(montant)
        else:
            print(f"Compte {numero_compte} non trouvé.")
    else:
        print(f"Client {identifiant_client} non trouvé.")

# Génération du numéro de compte à partir du numéro de client
generer_num_compte = lambda num_cl: int(str(num_cl) + str(random.randint(0, 100)))

def ecrire_fichier_csv(banque, nom_fichier):
    with open(nom_fichier, 'w', newline='') as csvfile:
        noms_champs = ['Client', 'Code Secret']
        writer = csv.DictWriter(csvfile, fieldnames=noms_champs)

        writer.writeheader()
        for client, code_secret in banque.secret_clients.items():
            writer.writerow({'Client': client, 'Code Secret': code_secret})
    print(f"Informations clients écrites dans {nom_fichier}.")

def manipuler_ensembles_listes_tuples(banque):
    ensemble_compte = set(banque.client_compte.values())
    liste_compte = list(ensemble_compte)
    tuple_compte = tuple(liste_compte)
    return liste_compte, tuple_compte, ensemble_compte

# Création de la banque
banque = Banque()

while True:
    print("\nMenu Principal :")
    print("1.
