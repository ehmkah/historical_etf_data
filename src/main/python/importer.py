import csv
import sys
import os
import uuid

def readCountries(filename):
    """Read and print the contents of a CSV file."""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    values = set()

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            val = row['Standort']
            stock = row['Anlageklasse']
            if val is not None and stock == 'Aktien':
                            val = val.strip()
                            if val:
                                values.add(val)

    for countryName in sorted(values):
        print(f"INSERT INTO countries (countryname) VALUES ('{countryName}');");

def readStocks(filename):
    """Read and print the contents of a CSV file."""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    values = []

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            countryName = row['Standort']
            stockName = row['Name']
            anlageKlasse = row['Anlageklasse']
            if countryName is not None and anlageKlasse == 'Aktien':
                countryName = countryName.strip()
                if countryName:
                    values.append({"stockName" : stockName, "countryName" : countryName})

    for stock in values:
        stockName = stock['stockName']
        countryName = stock['countryName']
        isin = uuid.uuid4()
        print(f"INSERT INTO stocks (stock_name, country_id, isin) VALUES ('{stockName}', (select id from countries where countryname='{countryName}'), '{isin}');")

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
            case "stocks":
                readStocks(csv_file)
