import random

while True:
    try:
        n= int(input("Level: "))
        #level entered must be valid (positive)
        if n>0:
            break
    except ValueError:
        pass

#random number between 1 and the level entered
number= random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        #check if guess is valid (bigger than 1)
        if guess<1:
            continue
        #conditionals involving the guess and random number
        if guess>number:
            print("Too large!")
        elif guess<number:
            print("Too small!")
        elif guess==number:
            print("Just right!")
            break

    except ValueError:
        pass
    except EOFError:
        break
