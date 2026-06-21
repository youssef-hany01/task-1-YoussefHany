password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    score += 1

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    score += 1

special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

has_symbol = False
for char in password:
    if char in special_chars:
        has_symbol = True
        break

if has_symbol:
    score += 1

if score <= 1:
    print("\nPassword Strength: Weak")
elif score <= 3:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Strong")

print("\nSuggestions:")

if len(password) < 8:
    print("- Password should be at least 8 characters")

if not has_upper:
    print("- Add an uppercase letter")

if not has_digit:
    print("- Add a number")

if not has_symbol:
    print("- Add a special character")

if score == 4:
    print("- Your password meets all basic strength requirements")