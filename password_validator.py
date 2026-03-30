import sys

# Allowed special characters
SPECIAL_CHARS = "!@#$%^&*()-_+="

# Main validation function
def validate_password(password):

    """
    Validates password against security rules.

    Rules:
    - must be string
    - at least 8 characters
    - no spaces
    - at least 1 uppercase letter
    - at least 1 lowercase letter
    - at least 1 digit
    - at least 1 special character from allowed set ("!@#$%^&*()-_+=")
    """

    # Trigger an error if the password is not a string
    if not isinstance(password, str):
        raise TypeError ("Password must be a string.")
    
    # Set tracking variables for conditions
    found_uppercase = False
    found_lowercase = False
    found_digit = False
    found_special = False
    
    # Check if no password was provided
    if password == "":
        return "Password is empty."
    
    # Check if the provided password contains a space
    if " " in password:
        return "Password may not contain any spaces."
    
    # Check if password is longer or equals 8 characters
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Loop through the provided password and check if there are at least one uppercase and lowercase letters, digit and a special character
    for char in password:
        if char.isupper():
            found_uppercase = True
        if char.islower():
            found_lowercase = True
        if char.isdigit():
            found_digit = True
        if char in SPECIAL_CHARS:
            found_special = True

    if not found_uppercase:
        return "Password needs to contain at least one uppercase letter."
    if not found_lowercase:
        return "Password needs to contain at least one lowercase letter."
    if not found_digit:
        return "Password needs to contain at least one digit."
    if not found_special:
        return "Password needs to contain at least one special character."
    return "valid"


# CLI entrypoint for running the validator from terminal
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python password_validator.py "YourPasswordHere"')
    else:
        password = sys.argv[1]
        print(validate_password(password))