total = 0
while total <50:
    #ask user for coin one at a time plus make it integer
    coin= int(input ("Insert a coin: "))

    if coin == 25 or coin == 10 or coin == 5:
    #add coin amount to the total
        total += coin

    if total< 50:
        due= 50 -total
        #output amount that is due
        print (f"Amount due: {due}")

#change that must be returned
change = total- 50
print (f"Change owed: {change}")


