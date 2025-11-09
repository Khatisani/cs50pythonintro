import sys
import csv

if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        firsts=[]
        lasts=[]
        house=[]
        try:
            with open(sys.argv[1],'r') as file:
                reader=csv.DictReader(file)
                for row in reader:
                    last, first=row['name'].split(',')
                    lasts.append(last.strip())
                    firsts.append(first.strip())
                    house.append(row['house'])
        except FileNotFoundError:
            exit('File does not exist')

        with open(sys.argv[2],'w') as file:
            fieldnames=['first','last','house']
            writer=csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(firsts)):
                writer.writerow({'first': firsts[i],'last': lasts[i],'house': house[i],})
