import string

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 5:
        return "Very Strong Password"
    elif strength >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"


password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)
