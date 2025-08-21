months= ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    date= input("Date: ").strip()
    if "/" in date:
            #for "9/8/1636" date format
        try:
            month, day, year =date.split("/")
            #make month,day and year integers
            month =int(month)
            day=int(day)
            year =int(year)

        except ValueError:
            pass
        else:
            #checking if the date is valid
            if month >12 or day>31:
                pass
            else:
                break
    else:
        #for "September 8, 1636" date format
        try:
            monthday, year =date.split(",")
            month, day=monthday.split()
            #make day and year integers
            day =int(day)
            year=int(year)
        except ValueError:
            pass
        else:
            month = months.index(month)+1
            #checking if the date entered is valid
            if month >12 or day>31:
                pass
            else:
                break

print(f"{year:04}-{month:02}-{day:02}")