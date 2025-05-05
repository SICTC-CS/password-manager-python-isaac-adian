class Account:
    def __init__(self, accountName, username, password, category):
        self.accountName = accountName
        self.username = username
        self.password = password
        self.category = category

    def display(self):
        """Print the account details in a simple output format."""
        print(f"\nThe account: {self.accountName}")
        print(f"The username: {self.username}")
        print(f"The password: {self.password}")
        print(f"Category: {self.category}")

    def editAccount(self):
        """Allow the user to edit account details."""
        print(f"\nEditing account: {self.accountName}")
        newUsername = input("Enter new username (or press Enter to keep current): ")
        newPassword = input("Enter new password (or press Enter to keep current): ")
        newCategory = input("Enter new category (or press Enter to keep current): ")

        if newUsername:
            self.username = newUsername
        if newPassword:
            self.password = newPassword
        if newCategory:
            self.category = newCategory
        print("Account updated successfully.")

    def toLine(self):
        """Convert account data into a savable string for a file."""
        return f"{self.accountName}|{self.username}|{self.password}|{self.category}\n"

    @staticmethod
    def fromLine(line):
        """Convert a line from the file back into an Account object."""
        accountName, username, password, category = line.strip().split("|")
        return Account(accountName, username, password, category)