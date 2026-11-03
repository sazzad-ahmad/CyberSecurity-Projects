
import string

print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

# User theke password input neya
password = input("Enter your password: ")

# Password er length check
length = len(password)

# Character types check
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

# Score calculation
score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# Result display
print("\n========== PASSWORD ANALYSIS ==========")

print("Password Length:", length)
print("Uppercase Letter:", "Yes" if has_upper else "No")
print("Lowercase Letter:", "Yes" if has_lower else "No")
print("Number:", "Yes" if has_digit else "No")
print("Special Character:", "Yes" if has_special else "No")

print("\nPassword Score:", score, "/ 6")

if score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

# Suggestions
print("\n========== SUGGESTIONS ==========")

if length < 12:
    print("- Use at least 12 characters.")

if not has_upper:
    print("- Add uppercase letters (A-Z).")

if not has_lower:
    print("- Add lowercase letters (a-z).")

if not has_digit:
    print("- Add numbers (0-9).")

if not has_special:
    print("- Add special characters (!@#$%).")

print("\nPassword analysis completed!")
print("=" * 45)
