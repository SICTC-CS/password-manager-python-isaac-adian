from account import Account
from passwordGenerator import PasswordGenerator
from passwordValidator import PasswordValidator 

class PasswordManager:
    def __init__(self):
        self.accounts = []  # List of Account objects

    def addAccount(self):
        print("\n--- Add a New Account ---")
        accountName = input("Enter the account name: ")
        username = input("Enter the username: ")

        while True:
            choice = input("Would you like to [G]enerate or [E]nter a password? ").lower()
            if choice == 'g':
                password = PasswordGenerator.generatePassword()
                print(f"Generated password: {password}")
                break
            elif choice == 'e':
                password = input("Enter your password: ")
                if PasswordValidator.isValid(password):
                    break
                else:
                    print("Password does not meet security requirements. Try again.")
            else:
                print("Invalid choice. Please enter G or E.")

        category = input("Enter a category (e.g., work, home, entertainment): ")
        newAccount = Account(accountName, username, password, category)
        self.accounts.append(newAccount)
        print("Account added successfully!")

    def viewAccountsByCategory(self):
        print("\n--- View Accounts by Category ---")
        categories = list(set(account.category for account in self.accounts))
        if not categories:
            print("No categories found.")
            return

        print("Available categories:")
        for i, cat in enumerate(categories):
            print(f"{i+1}. {cat}")

        choice = input("Enter category name to view: ")
        found = False
        for acc in self.accounts:
            if acc.category.lower() == choice.lower():
                acc.display()
                found = True
        if not found:
            print("No accounts found in that category.")

    def viewAllCategories(self):
        print("\n--- All Categories ---")
        categories = sorted(set(account.category for account in self.accounts))
        if not categories:
            print("No categories created yet.")
        else:
            for cat in categories:
                print(f"- {cat}")

    def deleteAccount(self):
        print("\n--- Delete an Account ---")
        name = input("Enter the account name to delete: ")
        for acc in self.accounts:
            if acc.accountName.lower() == name.lower():
                self.accounts.remove(acc)
                print("Account deleted.")
                return
        print("Account not found.")

    def editAccount(self):
        print("\n--- Edit an Account ---")
        name = input("Enter the account name to edit: ")
        for acc in self.accounts:
            if acc.accountName.lower() == name.lower():
                acc.editAccount()
                return
        print("Account not found.")

    def saveToFile(self, filename):
        with open(filename, "w") as f:
            for acc in self.accounts:
                f.write(acc.toLine())
        print(f"Accounts saved to {filename}.")

    def loadFromFile(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    account = Account.fromLine(line)
                    self.accounts.append(account)
            print(f"Loaded accounts from {filename}.")
        except FileNotFoundError:
            print("No saved account file found. Starting fresh.")