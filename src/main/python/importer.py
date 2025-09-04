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

def createValuationDate(valuationDate):
    """Create new valuadtionDate if it doesn't exist."""
    print(f"insert into valuation_dates (valuation_datetime) values ('{valuationDate}');")

def createFond(fondName):
    """Create new valuadtionDate if it doesn't exist."""
    isin = uuid.uuid4()
    print(f"insert into etfs (fond_name, isin) values ('{fondName}', '{isin}');")



def readHoldings(filename, etfName, valuationDate):
    """Read and print the contents of a CSV file."""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    values = []

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stockName = row['Name']
            countryName = row['Standort']
            allocationInPercentage = row['Gewichtung (%)']
            anlageKlasse = row['Anlageklasse']
            if countryName is not None and anlageKlasse == 'Aktien':
                countryName = countryName.strip()
                if countryName:
                    values.append({"stockName" : stockName,
                                   "allocationInPercentage" : allocationInPercentage})

    for stock in values:
        stockName=stock['stockName']

        allocationInPercentage = stock['allocationInPercentage'].replace(",", ".")
        stockQuery = f"(select id from stocks where stock_name='{stockName}' LIMIT 1)"
        etfQuery = f"(select id from etfs where fond_name='{etfName}' LIMIT 1)"
        valuationDateQuery = f"(select id from valuation_dates where valuation_datetime='{valuationDate}' LIMIT 1)"
        print(f"INSERT INTO holdings (valuation_date_id, etf_id, stock_id, allocation_percentage) VALUES ({valuationDateQuery}, {etfQuery}, {stockQuery}, {allocationInPercentage});")


if __name__ == "__main__":
    # Check for filename argument
    if len(sys.argv) < 5:
        print("Usage: python read_csv.py <type> <filename.csv> <etf_name> <valuation_date>")
        sys.exit(1)

    type = sys.argv[1]
    csv_file = sys.argv[2]
    etf_name = sys.argv[3]
    valuation_date = sys.argv[4]
    match type.lower():
            case "countries":
                readCountries(csv_file)
            case "stocks":
                readStocks(csv_file)
            case "holdings":
                readHoldings(csv_file, etf_name, valuation_date)
            case "createvaluationdate":
                createValuationDate(valuation_date)
            case "createfond":
                createFond(etf_name)
