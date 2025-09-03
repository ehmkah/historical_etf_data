import csv
import sys
import os

def read_csv(filename):
    """Read and print the contents of a CSV file."""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(f"--- Reading '{filename}' ---")
        for row in reader:
            print(row)

if __name__ == "__main__":
    # Check for filename argument
    if len(sys.argv) < 2:
        print("Usage: python read_csv.py <filename.csv>")
        sys.exit(1)

    csv_file = sys.argv[1]
    read_csv(csv_file)
