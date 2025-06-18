expr = str(input('Type the expression: '))
stack = [] #"stack" that will help to check the parentheses

for symbol in expr:
    if symbol == '(': # If you find an opening parenthesis
        stack.append('(') # Put on the stack
    elif symbol == ')': # If you find a closing parenthesis
        if len(stack) > 0: # Do you have anything to close?
            stack.pop() # Remove the last open
        else:
            stack.append(')') # mark the error
            break
if len(stack) == 0:
    print('Your expression is correct!')
else:
    print('Your expression is incorrect!')