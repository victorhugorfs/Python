headquarters = [[], [], []]

sum = third_col_sum = 0

for l in range(3):
    for c in range(3):
        value = int(input(f'Type one value for [{l}, {c}]: '))
        headquarters[l].append(value)

print('-='*30)
for line in headquarters:
    for item in line:
        print(f'[{item}]', end= ' ')
    print()
print('-='*30)

for line in headquarters:
    for item in line:
        if item % 2 == 0:
            sum += item
print(f'The sum of all even values ​​is {sum}')

for column in headquarters:
    third_col_sum += column[2]
print(f'The sum of the values ​​in the third column is {third_col_sum}')

print(f'The largest value in the second row is {max(headquarters[1])}')