#ask user or a greeting plus ignore whitespace plus make lower case
greeting= input('Enter a greeting: ').lower().strip()

#if it starts with hello output 0 dollars
if greeting.startswith('hello'):
    print ('$0')
#if it starts with h then output 20 dollrs
elif greeting[0] == 'h':
    print ('$20')
#otherwise output 100 dollars
else:
    print ('$100')