import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # 1. Check password length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")
        
    # 2. Check for Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter (A-Z).")
        
    # 3. Check for Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter (a-z).")
        
    # 4. Check for Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one number (0-9).")
        
    # 5. Check for Special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character (e.g., @, $, !, %, *, ?, &).")
        
    # Evaluate the result
    print("\n--- Password Strength Result ---")
    if score == 5:
        print("Strength: Strong 🟢")
    elif score >= 3:
        print("Strength: Moderate 🟡")
    else:
        print("Strength: Weak 🔴")
        
    if feedback:
        print("\nSuggestions (Areas to improve):")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    check_password_strength(user_password)
