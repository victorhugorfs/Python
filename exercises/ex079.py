numbers_list = []

numbers = int(input('Type one value: '))
print('Value added successfully...')
numbers_list.append(numbers)

while True:
    answer = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]

    if answer == 'Y':
        numbers = int(input('Type one value: '))
        if numbers in numbers_list:
            print('Duplicate value! Not added...')
        else:
            numbers_list.append(numbers)
            print('Value added successfully...')
    
    elif answer == 'N':
        numbers_list.sort()
        print(f'You typed these values: {numbers_list}')
        break
