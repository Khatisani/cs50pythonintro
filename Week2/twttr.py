#ask user to enter a text
text= input("Enter a text: ")
#list of all the vowels
vowels= ["a", "e", "i", "o", "u"]
#empty string for the new text
newtext= ""

for char in text:
    #if the lower case of a character is not a vowel
    if char.lower() not in vowels:
        #add the character to the newtext string
        newtext += char
print(newtext)
