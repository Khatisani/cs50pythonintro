#ask user for an expression
expression= input("Enter an expression: ").strip()
#split the expression
x, operator ,z= expression.split()
#make the numbers floats
x= float(x)
z= float(z)

#ouput reults
if operator == "+":
    answer= x+z
elif operator == "-":
    answer= x-z
elif operator == "*":
    answer= x*z
elif operator == "/":
    answer= x/z

#output results rounded to one decimal
print (f"{answer:.1f}")
