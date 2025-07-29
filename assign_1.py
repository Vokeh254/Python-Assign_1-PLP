First_num = int(input("Enter the first number: "))
Second_num = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == '+':
    result = First_num + Second_num
elif operator == '-':
    result = First_num - Second_num
elif operator == '*':
    result = First_num * Second_num 
elif operator == '/':
    if Second_num != 0:
        result = First_num / Second_num
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"    
    
print(f"your result is {First_num} {operator} {Second_num} = {result}") 