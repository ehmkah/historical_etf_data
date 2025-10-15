# Extracting ishares msci acwi ucits
# source : https://www.ishares.com/de/privatanleger/de/produkte/251850/

from importer import *

valuationDate = "2025-06-30"
fundName = "ishares_msci_acwi_ucits_etf"

### normally no modifications below that line

fileName = f"../../../data/{fundName}/{valuationDate}_adjusted.csv"

createFond(fundName)
createValuationDate(valuationDate)
createCountries(fileName)
createStocks(fileName)
createHoldings(fileName, fundName, valuationDate)

# python3 importer.py createFond ../../../data/ishares_msci_acwi_ucits_etf/2025-06-30.csv fundName valuationDate > fond.sql
# python3 importer.py createValuationDate ../../../data/ishares_msci_acwi_ucits_etf/2025-06-30.csv fundName valuationDate
# python3 importer.py countries ../../../data/ishares_msci_acwi_ucits_etf/2025-06-30.csv fundName valuationDate > countries.sql
# python3 importer.py stocks ../../../data/ishares_msci_acwi_ucits_etf/2025-06-30.csv fundName valuationDate >stocks.sql
# python3 importer.py holdings ../../../data/ishares_msci_acwi_ucits_etf/2025-06-30.csv fundName valuationDate >holdings.sql
