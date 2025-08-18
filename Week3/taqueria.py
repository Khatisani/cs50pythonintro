#dictionary of menu 
menu= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#starting point
total=0

while True:
    try:
        #user intput
        item =input("Item: ").strip().title()
        #add menu item price to total
        total +=menu[item]
        #display and round off to 2 places
        print(f"Total: ${total:.2f}")

    #if item is not in the menu, reprompt
    except KeyError:
        pass

    #contol+D is pressed
    except EOFError:
        #new line
        print("\n")
        break


