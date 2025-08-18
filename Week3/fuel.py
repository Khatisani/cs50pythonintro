
while True:
    try:

        #ask user for a fraction
        fraction= input("Fraction: ")
        #split into x/y
        x,y= fraction.split("/")
        x= int(x)
        y= int(y)

        if x>y or x<0:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError 

        #output as a percentage rounded to nearest integer
        percentage= round((x/y) *100)
        #if 1% or less output E
        if percentage <=1:
            print ('E')
        #if 99% output F
        elif percentage >=99:
            print ('F')
        else:
            print (f"{percentage}%")
        break

    except ValueError:
        print ("That's not a valid fraction")
    except ZeroDivisionError:
        print ("Division by 0 is not possible")