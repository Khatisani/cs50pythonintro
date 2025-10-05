def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #minimum of 2 characters and max 6
    if len(s)<2 or len(s)>6:
        return False
    #start with at least 2 letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    #no spaces or punctuation marks
    for char in s:
        if not char.isalnum():
            return False

    #digits at the end
    for i in range(len(s)):
        if s[i].isdigit():
            #first digit not a zero
            if s[i]== "0":
                return False
            #char are all digits onwards
            if not s[i:].isdigit():
                return False
            break
    #conditions met
    return True

if __name__ == "__main__":
    main()
