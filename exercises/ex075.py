value1 = int(input('Type one number: '))
value2 = int(input('Type another number: '))
value3 = int(input('Type another number: '))
value4 = int(input('Type one last number: '))

numbers = (value1, value2, value3, value4)

cont = numbers.count(9)

print(f'The number 9 appeared {cont} times.')

if 3 in numbers:
    print(f'Number 3 appeared first in position {numbers.index(3) + 1}.')
else:
    print('Number 3 was not entered.')

print('Even numbers:', end=' ')
for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')