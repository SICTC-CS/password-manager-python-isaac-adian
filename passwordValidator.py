class PasswordValidator:
    @staticmethod
    def isValid(password):
        """check if the password meets the following criteria:
        - At least 8 characters
        - Contains at least 1 uppercase letter
        - Contains at least 1 number
        - Contains at least 1 special character (!@#$%^&*)
        """
        if len(password) < 8:
            return False

        hasUpper = False
        hasNumber = False
        hasSpecial = False
        specialChars = "!@#$%^&*"

        for char in password:
            if char.isupper():
                hasUpper = True
            if char.isdigit():
                hasNumber = True
            if char in specialChars:
                hasSpecial = True

        return hasUpper and hasNumber and hasSpecial
        