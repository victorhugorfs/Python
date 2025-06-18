number_list = []

while True:
    value = int(input('Type one value: '))
    number_list.append(value)

    ask = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if ask == 'N':
        break

print(f'\nYou typed {len(number_list)} elements.')

number_list.sort(reverse=True)
print(f'The values in descending order are: {number_list}')

if 5 in number_list:
    print('The number 5 was found!')
else:
    print('The number 5 was not found.')