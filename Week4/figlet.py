from pyfiglet import Figlet
import random
import sys

figlet= Figlet()
#get list of fonts
fonts=figlet.getFonts()

    #zero arguments
if len(sys.argv) ==1:
    string=input("Input: ")
    randomf=random.choice(fonts)
    figlet.setFont(font=randomf)
    #print in random font
    print(f"Output:{figlet.renderText(string)}")

    #2 arguments and check if first is -f or --font
elif len(sys.argv)==3 and sys.argv[1] in ["-f", "--font"]:
    chosenf=sys.argv[2]
    if chosenf in fonts:
        string=input("Input: ")
        figlet.setFont(font=chosenf)
        #print in font that is chosen
        print(f"Output:{figlet.renderText(string)}")
    else:
        #argument/s doesn't meet conditions
        sys.exit("Invalid usage")
else:
    #incorrect arrgument numbers
    sys.exit("Invalid usage")
