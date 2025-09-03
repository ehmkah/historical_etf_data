import csv
import sys
import os

def readCountries(filename):
    """Read and print the contents of a CSV file."""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    values = set()

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(f"--- Reading '{filename}' ---")
        for row in reader:
            val = row['Standort']
            stock = row['Anlageklasse']
            if val is not None and stock == 'Aktien':
                            val = val.strip()
                            if val:
                                values.add(val)

    for countryName in sorted(values):
        print(f"INSERT INTO countries (countryname) VALUES ('{countryName}');");

if __name__ == "__main__":
    # Check for filename argument
    if len(sys.argv) < 3:
        print("Usage: python read_csv.py <filename.csv>")
        sys.exit(1)

    csv_file = sys.argv[1]
    type = sys.argv[2]
    match type.lower():
            case "countries":
                readCountries(csv_file)
