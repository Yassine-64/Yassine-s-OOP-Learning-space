import tkinter as tk
from tkinter import ttk
import json

class Compte:
    def __init__(self, numero, proprietaire, solde, date_ouverture):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde = solde
        self.date_ouverture = date_ouverture

    def get_numero(self):
        return self.numero

    def get_proprietaire(self):
        return self.proprietaire

    def get_solde(self):
        return self.solde

    def get_date_ouverture(self):
        return self.date_ouverture

    def __str__(self):
        return (f"Compte Numéro: {self.numero}, "
                f"Propriétaire: {self.proprietaire}, "
                f"Solde: {self.solde}, "
                f"Date d'Ouverture: {self.date_ouverture}")

class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde, date_ouverture, montant_decouvert_autorise):
        super().__init__(numero, proprietaire, solde, date_ouverture)
        self.montant_decouvert_autorise = montant_decouvert_autorise

    def get_montant_decouvert_autorise(self):
        return self.montant_decouvert_autorise

    def __str__(self):
        return (super().__str__() + 
                f", Montant Découvert Autorisé: {self.montant_decouvert_autorise}")

class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde, date_ouverture, interet):
        super().__init__(numero, proprietaire, solde, date_ouverture)
        self.interet = interet

    def get_interet(self):
        return self.interet

    def __str__(self):
        return (super().__str__() + 
                f", Intérêt: {self.interet}")

class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account Creation App")

        # Table to display the accounts
        self.accounts_table = ttk.Treeview(root, columns=("number", "owner", "balance", "type", "interest", "overdraft"), show="headings")
        self.accounts_table.grid(row=7, column=0, columnspan=2)
        self.accounts_table.heading("number", text="#")
        self.accounts_table.heading("owner", text="Propriétaire")
        self.accounts_table.heading("balance", text="Solde Initial")
        self.accounts_table.heading("type", text="Type")
        self.accounts_table.heading("interest", text="Taux Intérêt")
        self.accounts_table.heading("overdraft", text="Montant Découvert")

        # Variable dial bank account
        self.account_number = tk.IntVar(value=5)  # Starting from 5 as shown in the image
        self.owner_name = tk.StringVar()
        self.initial_balance = tk.StringVar()
        self.account_type = tk.StringVar(value="Courant")
        self.interest_rate = tk.StringVar()
        self.overdraft = tk.StringVar()

        self.account_type.trace('w', self.update_fields)

        # Load existing account data from JSON file
        self.load_accounts()

        tk.Label(root, text="Numéro:").grid(row=0, column=0, sticky="e")
        tk.Entry(root, textvariable=self.account_number, state='readonly').grid(row=0, column=1)

        tk.Label(root, text="Propriétaire:").grid(row=1, column=0, sticky="e")
        tk.Entry(root, textvariable=self.owner_name).grid(row=1, column=1)

        tk.Label(root, text="Solde Initial:").grid(row=2, column=0, sticky="e")
        tk.Entry(root, textvariable=self.initial_balance).grid(row=2, column=1)

        tk.Label(root, text="Type:").grid(row=3, column=0, sticky="e")
        tk.Radiobutton(root, text="Courant", variable=self.account_type, value="Courant").grid(row=3, column=1, sticky="w")
        tk.Radiobutton(root, text="Épargne", variable=self.account_type, value="Épargne").grid(row=3, column=1)

        tk.Label(root, text="Taux Intérêt").grid(row=4, column=0, sticky="e")
        self.interest_entry = tk.Entry(root, textvariable=self.interest_rate)
        self.interest_entry.grid(row=4, column=1)

        tk.Label(root, text="M. Découvert").grid(row=5, column=0, sticky="e")
        self.overdraft_entry = tk.Entry(root, textvariable=self.overdraft)
        self.overdraft_entry.grid(row=5, column=1)

        tk.Button(root, text="Création Compte", command=self.create_account).grid(row=6, column=1, pady=10)

    def update_fields(self, *args):
        if self.account_type.get() == "Épargne":
            self.overdraft_entry.config(state="disabled")
            self.interest_entry.config(state="normal")
        else:
            self.overdraft_entry.config(state="normal")
            self.interest_entry.config(state="disabled")

    def create_account(self):
        # Inserer new account f table 
        account = {
            "Numero": self.account_number.get(),
            "Proprietaire": self.owner_name.get(),
            "SoldeInitial": self.initial_balance.get(),
            "Type": self.account_type.get(),
            "TauxInteret": self.interest_rate.get() if self.account_type.get() == "Épargne" else "",
            "MontantDecouvert": self.overdraft.get() if self.account_type.get() == "Courant" else ""
        }
        self.accounts_table.insert("", "end", values=(
            account["Numero"],
            account["Proprietaire"],
            account["SoldeInitial"],
            account["Type"],
            account["TauxInteret"],
            account["MontantDecouvert"]
        ))
        # Incrementer l acoount number
        self.account_number.set(self.account_number.get() + 1)
        # Cleari l fields after la creation 
        self.owner_name.set("")
        self.initial_balance.set("")
        self.interest_rate.set("")
        self.overdraft.set("")
        # Save data accounts hhh
        self.save_accounts(account)

    def save_accounts(self, account):
        with open("accounts.json", "a") as file:
            json.dump(account, file)
            file.write("\n")

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as file:
                lines = file.readlines()
                for line in lines:
                    account = json.loads(line)
                    self.accounts_table.insert("", "end", values=(
                        account["Numero"],
                        account["Proprietaire"],
                        account["SoldeInitial"],
                        account["Type"],
                        account["TauxInteret"],
                        account["MontantDecouvert"]
                    ))
        except FileNotFoundError:
            pass


root = tk.Tk()
app = BankAccountApp(root)
root.mainloop()
