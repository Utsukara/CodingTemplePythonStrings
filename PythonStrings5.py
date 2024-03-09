import re

# 5. User Input Data Processor
# Objective:
# The aim of this assignment is to process and format user input data for a SaaS application's registration form.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format. Convert the entire email address to lowercase and replace any spaces with a period.

def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name must be at least 2 characters long.")

validate_name_length("J", "Doe")
validate_name_length("Jane", "D")


def check_password_complexity(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return
    if not re.search("[a-z]", password):
        print("Error: Password must contain at least one lowercase letter.")
        return
    if not re.search("[A-Z]", password):
        print("Error: Password must contain at least one uppercase letter.")
        return
    if not re.search("[0-9]", password):
        print("Error: Password must contain at least one number.")
        return
    print("Password meets complexity requirements.")

check_password_complexity("Password1")
check_password_complexity("pass")


def format_email(email):
    formatted_email = email.lower().replace(" ", ".")
    return formatted_email

formatted_email = format_email("JohnDoe@Example.Com ")
print(formatted_email)
