# 7. Interactive Help Desk Bot
# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

# Task 3: Auto-Response Generator
# For general help inquiries, create a script that generates an auto-response providing links to the FAQ section, support contact information, and a link to submit a ticket.

def commandParser(user_input):
    commands = {
        "help": "How can I assist you? For FAQs, visit [FAQ Link]. To contact support, email us at support@example.com.",
        "issue": "Please describe your issue in more detail.",
        "contact support": "You can reach our support team via email: support@example.com."
    }
    
    for command, response in commands.items():
        if command in user_input.lower():
            print(response)
            return command
    print("I'm sorry, I don't understand that command. Can you try again?")
    return None

user_input = input("How can I assist you today? ")
parsed_command = commandParser(user_input)



def issueCategorizer(issue_description):
    categories = {
        "login": "Login Issue",
        "performance": "Performance Issue",
        "error": "Error Report"
    }
    
    for keyword, category in categories.items():
        if keyword in issue_description.lower():
            print(f"Identified as a {category}.")
            return category
    
    print("Issue category not identified, escalating to support team.")
    return "General Support"

if parsed_command == "issue":
    issue_description = input("Please describe your issue: ")
    issueCategorizer(issue_description)


def generateAutoResponse(command):
    if command == "help":
        response = """
        Here's how you can get further assistance:
        - Visit our FAQ section here: [FAQ Link]
        - Contact our support team at support@example.com
        - Submit a ticket directly through our support portal: [Ticket Submission Link]
        """
        print(response)

if parsed_command == "help":
    generateAutoResponse(parsed_command)
