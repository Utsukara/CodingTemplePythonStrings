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

# 2. Product Review Analysis
# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

# Task 3: Review Summary
# Implement a script that takes the first 50 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

def highlight_keywords_in_reviews(reviews, keywords):
    
    for review in reviews:
        modified_review = review
        for keyword in keywords:
            # Check if the keyword is in the review
            if keyword in review.lower():
                # Replace keyword with uppercase version
                modified_review = modified_review.replace(keyword, keyword.upper())
                modified_review = modified_review.replace(keyword.capitalize(), keyword.upper())
        print(modified_review)

reviews = [
    "I thought the product was good but could be improved.",
    "This is an excellent product, and I highly recommend it!",
    "Unfortunately, my experience was bad due to a manufacturing defect.",
    "The quality is average, not what I expected at this price point.",
    "Received a damaged item, poor service from the company."
]

keywords = {"good", "excellent", "bad", "poor", "average"}

highlight_keywords_in_reviews(reviews, keywords)

def tally_sentiment(reviews, positive_words, negative_words):

    results = []

    for review in reviews:
        # Initialize counts for this review
        positive_count = 0
        negative_count = 0
        # Normalize the review to lowercase to make comparison case-insensitive
        words = review.lower().split()
        # Count positive and negative words
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
        
        results.append((positive_count, negative_count))

    return results

reviews = [
    "I thought the product was good and the quality excellent.",
    "This is an excellent product, and I highly recommend it!",
    "Unfortunately, my experience was bad due to a manufacturing defect.",
    "The quality is average, not what I expected at this price point.",
    "Received a damaged item, poor service from the company."
]

positive_words = {"good", "excellent", "recommend", "highly", "loved"}
negative_words = {"bad", "poor", "damaged", "defect", "average"}

sentiment_counts = tally_sentiment(reviews, positive_words, negative_words)

for review, (pos_count, neg_count) in zip(reviews, sentiment_counts):
    print(f"Review: \"{review}\" \nPositive words: {pos_count}, Negative words: {neg_count}\n")

def summarize_review(review):
    # Check if the review is shorter than or exactly 50 characters
    if len(review) <= 50:
        return review
    # If the review is longer than 50 characters, find the last space within the first 50 characters
    cutoff_point = review[:50].rfind(' ')
    # If there is no space, use the full 50 characters; otherwise, cut off at the last complete word
    if cutoff_point == -1:
        summary = review[:50]
    else:
        summary = review[:cutoff_point]
    
    return summary + "…"

reviews = [
    "I thought the product was good and the quality excellent. Really loved it!",
    "This is an excellent product, and I highly recommend it! Five stars.",
    "Unfortunately, my experience was bad due to a manufacturing defect. Not happy.",
    "The quality is average, not what I expected at this price point. Could be better.",
    "Received a damaged item, poor service from the company. Very disappointed."
]

for review in reviews:
    print(summarize_review(review))

# 3. Log File Formatter
# Objective:
# The aim of this assignment is to format and extract information from raw log files generated by a SaaS application to improve readability and analysis.

# Task 1: Timestamp Extraction
# Write a script that extracts the timestamp from each log entry. Assume that the timestamp is always at the beginning of each line and is enclosed in square brackets (e.g., "[2023-03-15 10:00:00]").

# Task 2: Error Identification
# Create a function that scans through the log file and identifies any error messages. Assume that all error messages start with the word "ERROR:". The function should print out each error message with its corresponding timestamp.

# Task 3: Log Summary
# Develop a script that creates a summary of the log file, including the total number of entries, the number of error messages, and the number of unique timestamps in the file.

def extract_timestamps(log_entries):
    timestamps = [entry.split(']')[0][1:] for entry in log_entries]
    return timestamps

log_entries = [
    "[2023-03-15 10:00:00] INFO: User login successful.",
    "[2023-03-15 10:05:00] ERROR: Failed to connect to database.",
    "[2023-03-15 10:10:00] INFO: Data backup completed successfully."
]

timestamps = extract_timestamps(log_entries)
print("Extracted Timestamps:")
for timestamp in timestamps:
    print(timestamp)


def identify_errors(log_entries):
    for entry in log_entries:
        if "ERROR:" in entry:
            timestamp = entry.split(']')[0][1:]
            error_message = entry.split("ERROR:")[1].strip()
            print(f"{timestamp} - ERROR: {error_message}")

print("\nIdentified Error Messages:")
identify_errors(log_entries)


def log_summary(log_entries):
    total_entries = len(log_entries)
    error_count = sum(1 for entry in log_entries if "ERROR:" in entry)
    unique_timestamps = len(set(extract_timestamps(log_entries)))

    print(f"Log Summary:\nTotal Entries: {total_entries}\nError Messages: {error_count}\nUnique Timestamps: {unique_timestamps}")

print("\nLog File Summary:")
log_summary(log_entries)

# 4. Configuration File Validator
# Objective:
# The aim of this assignment is to validate and correct a SaaS application's configuration files to ensure they adhere to the required format.

# Task 1: Property Format Checker
# You are given a configuration file where each line contains a property and its value separated by an "=" sign. Write a script that checks each line to ensure it follows this format. If a line does not contain an "=" sign or has more than one, print an error message with the line number.

# Task 2: Whitespace Remover
# Modify the script from Task 1 to remove any leading or trailing whitespace from the property names and values.

# Task 3: Duplicate Property Finder
# Extend the script to check for duplicate property names. If a duplicate is found, print out the property name and the line numbers where the duplicates are located.

# 5. User Input Data Processor
# Objective:
# The aim of this assignment is to process and format user input data for a SaaS application's registration form.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format. Convert the entire email address to lowercase and replace any spaces with a period.

# 6. Text-Based Report Generator
# Objective:
# The aim of this assignment is to generate a formatted text-based report from raw data for a SaaS application's internal use.

# Task 1: Header Formatter
# Write a script that formats the headers of the report. Each header should be centered, in uppercase, and underlined with "=" characters.

# Task 2: Data Alignment
# Format the raw data so that each column is aligned. Assume the data is separated by commas and should be displayed in a table format with each value left-aligned in its column.

# Task 3: Report Summary
# At the end of the report, add a summary section that counts the number of data entries and calculates the average value of a numeric column.

# 7. Interactive Help Desk Bot
# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

# Task 3: Auto-Response Generator
# For general help inquiries, create a script that generates an auto-response providing links to the FAQ section, support contact information, and a link to submit a ticket.
