import csv
import os

# Define the directory and filename
directory = "csv files"
filename = "adjectives_nouns.csv"

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Full path for the CSV file
csv_path = os.path.join(directory, filename)

# Data for adjectives and nouns (30 distinct pairs)
data = [
    ("Trendy", "Corner"), ("Lively", "Market"), ("Bright", "Path"), ("Cozy", "Nook"), ("Charming", "Alley"),
    ("Elegant", "Boulevard"), ("Quaint", "Village"), ("Bustling", "Street"), ("Cheerful", "Cafe"), ("Serene", "Garden"),
    ("Vibrant", "Plaza"), ("Dynamic", "Hub"), ("Graceful", "Arcade"), ("Majestic", "Terrace"), ("Inviting", "Lounge"),
    ("Glowing", "Lantern"), ("Welcoming", "Entrance"), ("Peaceful", "Haven"), ("Chic", "Boutique"), ("Stylish", "Parlor"),
    ("Radiant", "Beacon"), ("Artistic", "Studio"), ("Magical", "Realm"), ("Rustic", "Cabin"), ("Picturesque", "Harbor"),
    ("Whimsical", "Pavilion"), ("Coastal", "Retreat"), ("Hidden", "Gem"), ("Crisp", "Morning"), ("Sunny", "Veranda")
]

# Writing to the CSV file
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Adjectives", "Noun"])  # Writing the header
    writer.writerows(data)  # Writing the rows

# Return the file path for user reference
csv_path
