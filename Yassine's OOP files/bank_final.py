import random
import csv

#
class Banque:
    # Initialiser les dict, kola dict 3ndha en face l key o value dialha sous forme de comment
    def __init__(self):
        self._clients = {}         #(numéro client -> code secret)
        self._comptes = {}          #(numéro compte -> solde)
        self._clients_comptes = {}   #(numéro client -> numéro compte)

    # Méthode bach n ajouter wahd client jdid
    def ajouter_client(self, num_cl, mpc, num_c, solde_c):
        self._clients[num_cl] = mpc
        self._comptes[num_c] = solde_c
        self._clients_comptes[num_cl] = num_c

    # Méthode bach n supprimer unn client
    def supprimer_client(self, num_c):
        # bach nfiltriw o nl9aw numero de cl associer l dak num de compte
        num_cl = [key for key, value in self._clients_comptes.items() if value == num_c]
        # if num cl = ila kant valeur existe donc
        if num_cl:
            # delete dict dial client 
            del self._clients[num_cl]
            # Supprimer compte mn dict compte 
            del self._comptes[num_c]
            del self._clients_comptes[num_cl]
        else:
            print(f"aucun compte trouvé")
    # pour changer le mdp
    def modifier_mp_client(self, num_cl, nouveau_mp):
        if num_cl in self._clients:
            self._clients[num_cl] = nouveau_mp

    # bach t7t flous ( self._comptes[num_c] += montant)
    def deposer(self, num_c, montant):
        if num_c in self._comptes:
            self._comptes[num_c] += montant

    # pour retirer l argent 
    def retirer(self, num_c, montant):
        if num_c in self._comptes and self._comptes[num_c] >= montant:
            self._comptes[num_c] -= montant

    # lambda pour generer num compte mn library dial random 
    generer_num_compte_lambda = lambda self, num_cl: int(str(num_cl) + str(random.randint(0, 100)))

    # pour ecrire info client dans un fichier csv
    def ecrire_fichier_csv(self):
        #bach n7l fichier en mode ecriture (w)
        with open('clients.csv', 'w', newline='') as csvfile:
            # les noms de champs 
            fieldnames = ['Numéro Client', 'Code Secret']
            # objet dictwriter bach nktbo f dak ficher 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # l entete dial fichier fiha num cl et code secret
            writer.writeheader()
            # bach nktb  chaque paire (num cl et mdp) f fichier CSV
            for num_cl, code_secret in self._clients.items():
                writer.writerow({'Numéro Client': num_cl, 'Code Secret': code_secret})

    # Méthode dial set liste o tuples 
    def manipuler_sts(self):
        liste_num_comptes = list(self._clients_comptes.values())
        tuple_num_comptes = tuple(self._clients_comptes.values())
        set_num_comptes = set(self._clients_comptes.values())

        return liste_num_comptes, tuple_num_comptes, set_num_comptes

    # Getters pour les attributs privés
    def get_clients(self):
        return self._clients

    def get_comptes(self):
        return self._comptes

    def get_clients_comptes(self):
        return self._clients_comptes

# Partie dial menu principal wsto menu dial client avec les fct depo retirer et modifer mdp 
banque = Banque()

while True:
    print("Menu :")
    print("1. Ajouter un Compte")
    print("2. Supprimer un Compte")
    print("3. Acceder au compte client")
    print("4. Quitter")

    choix = int(input("Choisissez une option: "))

    if choix == 1:
        numCl = int(input("Numéro du client: "))
        MPC = input("Code secret: ")
        numC = banque.generer_num_compte_lambda(numCl)
        SoldeC = float(input("Solde initial du compte: "))
        banque.ajouter_client(numCl, MPC, numC, SoldeC)
        print("Compte créé avec succès")

    elif choix == 2:
        numC = int(input("Numéro du compte à supprimer: "))
        banque.supprimer_client(numC)
        print("Compte supprimé avec succès")

    elif choix == 3:
        numCl = int(input("Numero du client: "))
        mdp = input("Code secret: ")

        if numCl in banque.get_clients() and mdp == banque.get_clients()[numCl]:
            while True:
                print("Menu client:")
                print("1. Modifier son mot de passe")
                print("2. Afficher son solde")
                print("3. Deposer une somme d argent")
                print("4. Retirer une somme d argent")
                print("5. Quitter")

                choix_client = int(input("Choisissez une option: "))

                if choix_client == 1:
                    nouveau_mdp = input("Nouveau mot de passe: ")
                    banque.modifier_mp_client(numCl, nouveau_mdp)
                    print("Votre nouveau mot de passe est créé")

                elif choix_client == 2:
                    num_client = banque.get_clients_comptes()[numCl]
                    #numéro de compte associé au numéro de client 
                    if num_client in banque.get_comptes():
                        # bach n accediw l solde dial compte associer l num client f dict dial compte
                        solde = banque.get_comptes()[num_client]
                        print(f"Solde actuel: {solde} Dh")

                elif choix_client == 3:
                    montant = float(input("Montant à déposer: "))
                    banque.deposer(banque.get_clients_comptes()[numCl], montant)
                    print("Depot effectue avec succes")

                elif choix_client == 4:
                    montant = float(input("Montant à retirer: "))
                    banque.retirer(banque.get_clients_comptes()[numCl], montant)
                    print("Retrait effectue avec succes")

                elif choix_client == 5:
                    print("Retour au menu principal .")
                    break

                else:
                    print("Option invalide")

        else:
            print("Numero de client ou mot de passe incorrect.")

    elif choix == 4:
        banque.ecrire_fichier_csv()
        print("bslama")
        break

    else:
        print("Option invalide")
