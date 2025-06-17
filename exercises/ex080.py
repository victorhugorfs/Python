value = []

for i in range(5):
    numbers = int(input('Type one number: '))
    pos = 0

    if len(value) == 0 or numbers > value[-1]:
        value.append(numbers)
        print(f'Added in position {len(value) - 1} of the list...')
    else:
        while pos < len(value) and numbers > value[pos]:
            pos += 1
        value.insert(pos, numbers)
        print(f'Added in position {pos} of the list...')

print('-=' * 30)
print(f'The values in order are: {value}')