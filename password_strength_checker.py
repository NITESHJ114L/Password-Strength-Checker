import re

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase letter
if re.search(r"[A-Z]", password):
    score += 1

# Check lowercase letter
if re.search(r"[a-z]", password):
    score += 1

# Check number
if re.search(r"[0-9]", password):
    score += 1

# Check special character
if re.search(r"[^A-Za-z0-9]", password):
    score += 1

print("\nPassword Analysis")
print("-----------------")

print("Length:", "Good" if len(password) >= 8 else "Too Short")
print("Uppercase:", "Yes" if re.search(r"[A-Z]", password) else "No")
print("Lowercase:", "Yes" if re.search(r"[a-z]", password) else "No")
print("Number:", "Yes" if re.search(r"[0-9]", password) else "No")
print("Special Character:", "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No")

if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print("\nStrength:", strength)