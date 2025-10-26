import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a python file")


name = sys.argv[1]
count = 0

try:
    with open(name, "r") as f:
        for line in f:
            if line.isspace():
                continue
            if line.strip().startswith('#'):
                continue
            count +=1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
