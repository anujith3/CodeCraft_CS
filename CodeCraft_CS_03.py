import re

def password_strength(password):
    length_criteria = len(password) >= 8
    lower_criteria = re.search(r'[a-z]', password) is not None
    upper_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria])

    if len(password) == 0:
        return "Password cannot be empty."
    elif score == 5:
        return "Very Strong password!"
    elif score == 4:
        return "Strong password."
    elif score == 3:
        return "Medium strength. Consider adding more variety (uppercase, digits, special characters)."
    elif score == 2:
        return "Weak password. Consider lengthening it and adding more types of characters."
    else:
        return "Very weak password. Use at least 8 characters, with uppercase, lowercase, numbers, and symbols."

password = input("Enter your password: ")
feedback = password_strength(password)
print(feedback)
