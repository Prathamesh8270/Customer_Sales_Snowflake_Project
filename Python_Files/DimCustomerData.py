import csv
import random
import os  # Import os module for directory handling
from faker import Faker

# Initialize Faker
fake = Faker()

# Input the number of rows for the CSV file
num_rows = int(input("Enter the number of rows the CSV file should have: "))

# Input the name of the CSV file (ensure it ends with .csv)
csv_file = input("Enter the name of the CSV file (e.g., data.csv): ")
if not csv_file.endswith(".csv"):
    csv_file += ".csv"  # Ensure it has the .csv extension

# Define the directory path
directory = "csv files"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Full path for the CSV file
csv_path = os.path.join(directory, csv_file)

# Open and write to the CSV file
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Create the header
    header = [
        'First Name', 'Last Name', 'Gender', 'DateOfBirth', 'Email', 
        'Phone Number', 'Address', 'City', 'State', 'Postal Code', 
        'Country', 'LoyaltyProgramID'
    ]
    
    # Write the header to the CSV file
    writer.writerow(header)

    # Loop and generate multiple rows
    for _ in range(num_rows):
        row = [
            fake.first_name(),
            fake.last_name(),
            random.choice(['M', 'F']),
            fake.date(),
            fake.email(),
            fake.phone_number(),
            fake.address().replace(",", " ").replace("\n", " "),  # Ensure proper formatting
            fake.city(),
            fake.state(),
            fake.postcode(),
            fake.country(),
            random.randint(1, 5)
        ]
        writer.writerow(row)

print(f"The file '{csv_file}' has been successfully saved in '{directory}'!")
