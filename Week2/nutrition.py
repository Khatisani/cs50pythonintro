#ask user for fruit and make it lower case
fruit= input("Enter a fruit: ").lower()

#dictionariy of fruits and calories
calories= {"apple":130,
    "avocado":50,
    "banana": 10,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "honeydew melon":50,
    "kiwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon":80}

#check if the entered fruit is in the dictionary
if fruit in calories:
    #output the value of the key which is the entered fruit
    print(f"Calories: {calories[fruit]}")