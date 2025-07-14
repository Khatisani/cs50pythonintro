#define function convert and conversion
def convert(message):
    message =message.replace(":)" , "🙂").replace(":(" , "🙁")
    return message

#main function
def main():
    #user input
    message= input("Please enter a message: ")
    print(convert(message))

main()
