#ask user to name in camel case
variable= input("Name of variable in camelCase: ")

#convert to snake case
snakecase= ""

for char in variable:
#if a character is in uppercase
    if char.isupper():
#add underscore to the string and make it lowercase
        snakecase += "_"
        snakecase += char.lower()
#otherwise add the character to the string unchanged
    else:
        snakecase += char

print(f"Snake_case: {snakecase}")