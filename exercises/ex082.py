list1 = []
list2 = []
list3 = []

while True:
    value = int(input('Type one value: '))
    list1.append(value)

    ask = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if ask == 'N':
        break

print(f'The full list is: {list1}')

for value in list1:
    if value % 2 == 0:
       list2.append(value)
    else:
        list3.append(value)

print(f'The list of pairs is: {list2}')
print(f'The list of odd is: {list3}')