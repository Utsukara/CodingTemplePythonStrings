# 1. Customer Data Sanitization
# Objective:
# The aim of this assignment is to practice string manipulation techniques by cleaning and formatting raw customer data extracted from a SaaS application's database.

# Task 1: Code Correction
# You are provided with a script that is supposed to format customer names by ensuring the first letter is uppercase and the rest are lowercase, regardless of how the data was entered. However, the script contains errors. Correct the script so that it functions as intended.

# Task 2: Email Validation
# Write a function that checks a list of email addresses for a SaaS application's user accounts. The function should verify that each email contains an "@" symbol and a "." after it, indicating a valid email format. If an email doesn't meet this criterion, print it out for further review.

# Task 3: Username Generation
# Create a script that generates a username for each new user. The username should be a combination of the first three letters of their first name and the first three letters of their last name. If the name is shorter than three letters, use the full name. Ensure all usernames are in lowercase.

def format_customer_name(name):   
    return name.title()

formatted_name = format_customer_name("jOhN dOe")
print(formatted_name)


def check_email_list(emails):   
    for email in emails:
        if "@" in email and "." in email.split("@")[-1]:
            continue
        else:
            print(f"Review email: {email}")

email_list = [
    "user@example.com",
    "invalidemail.com",
    "another.user@website",
    "valid.email@example.co.uk",
    "noatsymbol.net",
    "no.dot@com"
]
check_email_list(email_list)

def generate_username(first_name, last_name):
    # Extract the first three letters of the first name, or the full name if it's shorter than three letters
    first_part = first_name[:3]
    # Extract the first three letters of the last name, or the full name if it's shorter than three letters
    last_part = last_name[:3]
    # Combine the parts and convert to lowercase
    username = (first_part + last_part).lower()
    
    return username

usernames = [
    generate_username('Alexander', 'Hamilton'),
    generate_username('El', 'Burr'),
    generate_username('Thomas', 'Jefferson')
]

for username in usernames:
    print(username)