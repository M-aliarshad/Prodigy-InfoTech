import re

def assess_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score based on criteria met
    strength_score = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                          digit_criteria, special_char_criteria])

    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
        feedback = "Your password is very strong! Great job!"
    elif strength_score == 4:
        strength_level = "Strong"
        feedback = "Your password is strong, but consider adding more variety."
    elif strength_score == 3:
        strength_level = "Moderate"
        feedback = "Your password is moderate. Try to add more complexity."
    elif strength_score == 2:
        strength_level = "Weak"
        feedback = "Your password is weak. Please include more character types."
    else:
        strength_level = "Very Weak"
        feedback = "Your password is very weak. Consider using a mix of letters, numbers, and symbols."

    return strength_level, feedback

def main():
    print("Welcome to the Alis's Password Strength Assessment Tool!")
    
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Thank you for using the Ali's Password Strength Assessment Tool. Goodbye!")
            break
        
        strength_level, feedback = assess_password_strength(password)
        
        print(f"\nPassword Strength Level: {strength_level}")
        print(feedback)
        print("-" * 50)

if __name__ == "__main__":
    main()