import getpass

class User:
    def __init__(self, username, password, hint, firstName, lastName):
        self.username = username
        self.password = password
        self.hint = hint
        self.firstName = firstName
        self.lastName = lastName

    @staticmethod
    def registerUser():
        print("\n--- New User Registration ---")
        username = input("Enter a username: ")
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name: ")
        while True:
            password = getpass.getpass("Create a password: ")
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("Passwords do not match. Try again.")
            else:
                break
        hint = input("Enter a password hint (used if you forget): ")
        return User(username, password, hint, firstName, lastName)

    def loginUser(self):
        print("\n--- Log In ---")
        attempts = 3
        while attempts > 0:
            enteredPassword = getpass.getpass("Enter your password: ")
            if enteredPassword == self.password:
                print(f"Welcome back, {self.firstName}!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect password. Hint: {self.hint}")
                print(f"Attempts remaining: {attempts}")
        print("Too many failed attempts. Program shutting down.")
        return False

    def toLine(self):
        #Convert the user object to a storable string.
        return f"{self.username}|{self.password}|{self.hint}|{self.firstName}|{self.lastName}\n"

    @staticmethod
    def fromLine(line):
        #Convert a stored line back to a User object.
        username, password, hint, firstName, lastName = line.strip().split("|")
        return User(username, password, hint, firstName, lastName)