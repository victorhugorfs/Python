data0 = dict()
data1 = list()

for c in range(1):
    data0['name'] = str(input('Name: '))
    data0['average'] = float(input('Average: '))
    data1.append(data0.copy())

print(f'The name is {data0['name']}')
print(f'The average is {data0['average']}')

if data0['average'] >= 7.0:
    print(f'Status is equal to Approved')
else:
    print(f'Status is equal to Reproved')