import random

def main():
    level=get_level()
    score=0

    for i in range(10):
            x=generate_integer(level)
            y=generate_integer(level)
            answer=x+y
            wrong=0

            while True:
                try:
                    guess=int(input(f"{x} + {y} ="))
                except ValueError:
                    print ("EEE")
                    wrong+=1
                else:
                    if guess==answer:
                        score+=1
                        break
                    else:
                        print("EEE")
                        wrong+= 1
                if wrong==3:
                    print(f"{x} + {y} = {answer}")
                    break
    print("Score:", score)

#ask user for level and return 1,2 or 3
def get_level():
    while True:
        try:
            level=int(input("Level: "))
        except ValueError:
            continue
        else:
            if level==1 or level==2 or level==3:
                return level

#generate a random positive integer with level digits
def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
