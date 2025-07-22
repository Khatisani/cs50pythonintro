def main():
    #what time is it in 24-hour format
    inputted_time= input("Enter a time in 24-hour format: ").strip()
    hour= convert(inputted_time)

    #conditions
    if hour>=7.0 and hour<=8.0:
        print ("Breakfast time")
    elif hour>=12.0 and hour<=13.0:
        print ("Lunch time")
    elif hour>=18.0 and hour<=19.0:
        print ("Dinner time")


def convert(time):
    #split the input
    #minutes and hours separated by :
    hours, minutes = time.split(":")
    #make hrs and minutes floats
    hours= int(hours)
    minutes=int(minutes)
    return hours+minutes /60


if __name__ == "__main__":
    main()
