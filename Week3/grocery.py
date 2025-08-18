#create empty dictionary
groceries= {}

while True:
    try:
        #user input and make it uppercase
        item = input("").strip().upper()
        if item not in groceries:
            #add new items to dictionary
            groceries[item]=1
        else:
            #add 1 when the item is entered again
            groceries[item]+=1

    #when control+D is pressed
    except EOFError:
        #sort the dict in alphabetical order
        ordered= sorted(groceries)
        for item in ordered:
            #print the item and its number
            print (groceries[item], item)
        break
    #if item is not in the list, reprompt
    except KeyError:
        pass


