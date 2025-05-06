import random
from faker import Faker
import sqlite3
import csv

# Initialize Faker
fake = Faker()

def generate_fake_person():
    name = fake.name()
    # Create a simple email ID based on the name
    username = name.lower().replace(' ', '.')
    domain = random.choice(['example.com', 'mycompany.net', 'mail.org', 'webmail.in'])
    email = f"{username}@{domain}"
    return name, email

def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        name, email = generate_fake_person()
        data.append((name, email))
    return data


def export_to_csv(data, filename="random_customers_289.csv"):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Customer Name', 'Email'])
        writer.writerows(data)
    print(f"Successfully exported {len(data)} records to '{filename}'.")

if __name__ == "__main__":
    num_records = 289
    random_data = generate_random_data(num_records)

    # Option 2: Export to a CSV file
    export_to_csv(random_data, filename="random_customers_289.csv")

    print("Generated and processed 289 random names and email IDs.")
