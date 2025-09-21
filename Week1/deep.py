#ask the question plus make it lower case plus remove whitespace
answer= input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
#conditions are true
if answer == '42' or answer == 'forty two' or answer == 'forty-two':
    print ('Yes')
else:
    print ('No') #conditions are false
