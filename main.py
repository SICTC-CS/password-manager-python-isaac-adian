from user import User
from passwordManager import PasswordManager

USER_FILE = "user.txt"
ACCOUNT_FILE = "accounts.txt"

def loadUser():
    try:
        with open(USER_FILE, "r") as f:
            line = f.readline()
            if line:
                return User.fromLine(line)
    except FileNotFoundError:
        return None

def saveUser(user):
    with open(USER_FILE, "w") as f:
        f.write(user.toLine())

def main():
    print("=== Welcome to the Password Manager ===")
    existingUser = loadUser()

    if existingUser is None:
        print("No existing user found. Please register.")
        user = User.registerUser()
        saveUser(user)
        print("Registration complete. Please log in.")
        if not user.loginUser():
            return
    else:
        print(f"Welcome back, {existingUser.firstName}. Please log in.")
        if not existingUser.loginUser():
            return
        user = existingUser

    manager = PasswordManager()
    manager.loadFromFile(ACCOUNT_FILE)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new account")
        print("2. View accounts by category")
        print("3. View all categories")
        print("4. Edit an account")
        print("5. Delete an account")
        print("6. Save and exit")
        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            manager.addAccount()
        elif choice == "2":
            manager.viewAccountsByCategory()
        elif choice == "3":
            manager.viewAllCategories()
        elif choice == "4":
            manager.editAccount()
        elif choice == "5":
            manager.deleteAccount()
        elif choice == "6":
            manager.saveToFile(ACCOUNT_FILE)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()