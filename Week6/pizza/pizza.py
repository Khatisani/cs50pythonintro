import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

name = sys.argv[1]

try:
    with open(name, 'r') as f:
        reader = csv.reader(f)
        table = tabulate(reader, headers="firstrow", tablefmt="grid")
        print (table)

except FileNotFoundError:
    sys.exit("File does not exist.")
