# 4. Configuration File Validator
# Objective:
# The aim of this assignment is to validate and correct a SaaS application's configuration files to ensure they adhere to the required format.

# Task 1: Property Format Checker
# You are given a configuration file where each line contains a property and its value separated by an "=" sign. Write a script that checks each line to ensure it follows this format. If a line does not contain an "=" sign or has more than one, print an error message with the line number.

# Task 2: Whitespace Remover
# Modify the script from Task 1 to remove any leading or trailing whitespace from the property names and values.

# Task 3: Duplicate Property Finder
# Extend the script to check for duplicate property names. If a duplicate is found, print out the property name and the line numbers where the duplicates are located.

config_lines = [
    "api_key=123456789",
    "db_host=localhost",
    "db_port = 3306",
    "timeout=30",
    "error_log_path=/var/log/app_error.log",
    "cache_enabled=true",
    "cache_size=invalid line without equal sign",
    "debug_mode=true=another invalid line with multiple equals",
    "error_log_path=/var/log/app_error.log"
]

def check_format_and_process_lines(config_lines):
    properties = {}
    format_errors = []
    for i, line in enumerate(config_lines, 1):
        if line.count("=") != 1: #check for proper formatting
            format_errors.append(f"Error in line {i}: '{line}' - Invalid format.")
            continue
        key, value = line.split("=", maxsplit=1)
        key, value = key.strip(), value.strip()  # Remove leading/trailing whitespace
        if key in properties:
            properties[key].append((value, i))
        else:
            properties[key] = [(value, i)]
    
    for error in format_errors:
        print(error)
    
    return properties

def find_duplicates(properties):
    for key, occurrences in properties.items():
        if len(occurrences) > 1:
            line_numbers = ", ".join(str(line_num) for _, line_num in occurrences)
            print(f"Duplicate property '{key}' found at lines {line_numbers}.")

properties = check_format_and_process_lines(config_lines)
find_duplicates(properties)

