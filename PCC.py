print("//////////////////////////////////////////////////////////")
print("              Password Complexity Checker")
print("//////////////////////////////////////////////////////////")
print(" ")

password = input("Enter your Password to check its Strength:")

def check_password(password):
    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    suggestions = []

    # check length
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) > 12:
        score += 2

    # loop through password
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():  # special character
            has_special = True

    # assign points
    if has_upper: 
        score += 2
    else: 
        suggestions.append("Add an uppercase letter")

    if has_lower: 
        score += 2
    else: 
        suggestions.append("Add a lowercase letter")

    if has_digit: 
        score += 2
    else: 
        suggestions.append("Add a number")

    if has_special: 
        score += 2
    else: 
        suggestions.append("Add a special character")

    # final strength check
    if score <= 4:
        print("Strength Level: Weak")
    elif score <= 8:
        print("Strength Level: Medium")
    else:
        print("Strength Level: High")
        
    if suggestions:
        print("Suggestions:", ", ".join(suggestions))

    return score

final_score = check_password(password)
print("Password Score:", final_score)
