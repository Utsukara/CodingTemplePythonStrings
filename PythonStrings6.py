# 6. Text-Based Report Generator
# Objective:
# The aim of this assignment is to generate a formatted text-based report from raw data for a SaaS application's internal use.

# Task 1: Header Formatter
# Write a script that formats the headers of the report. Each header should be centered, in uppercase, and underlined with "=" characters.

# Task 2: Data Alignment
# Format the raw data so that each column is aligned. Assume the data is separated by commas and should be displayed in a table format with each value left-aligned in its column.

# Task 3: Report Summary
# At the end of the report, add a summary section that counts the number of data entries and calculates the average value of a numeric column.



def format_header(header):
    formatted_header = header.upper().center(20)
    underline = "=" * len(formatted_header)
    return f"{formatted_header}\n{underline}"

headers = ["Name", "Age", "Position"]
for header in headers:
    print(format_header(header))



data = [
    ["John Doe", 28, "Software Engineer"],
    ["Jane Smith", 32, "Data Scientist"],
    ["Dave Wilson", 45, "Product Manager"]
]

def format_data_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        formatted_row = " | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths))
        print(formatted_row)

format_data_table(data)



def report_summary(data):
    num_entries = len(data)
    average = sum(int(row[1]) for row in data) / num_entries
    print(f"\nSummary:\nTotal Entries: {num_entries}\nAverage Age: {average:.2f}")

report_summary(data)
