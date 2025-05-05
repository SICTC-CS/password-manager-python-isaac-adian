import random
import string

class PasswordGenerator:
    @staticmethod
    def generatePassword(length=12):
        """Generate a strong password meeting the following criteria:
        - At least 1 uppercase letter
        - At least 1 number
        - At least 1 special character (!@#$%^&*)
        - At least 8 characters long
        """
        if length < 8:
            print("Password must be at least 8 characters long.")
            return None

        # Define character sets
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&*")
        lower = ''.join(random.choices(string.ascii_lowercase, k=length - 3))

        # Combine and shuffle
        passwordList = list(upper + digit + special + lower)
        random.shuffle(passwordList)
        return ''.join(passwordList)