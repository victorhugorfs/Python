data0 = dict()
data1 = list()

while True:
    data0['name'] = str(input('Name: '))
    data0['sex'] = str(input('Sex: [M/F] ')).strip().upper()[0]
    data0['age'] = int(input('Age: '))

    data1.append(data0.copy())

    yorn = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
    if yorn == 'N':
        break

print('-=-'*30)

print(f'- The group has {len(data1)} people.')

total_age = sum(p['age'] for p in data1)
average_age = total_age / len(data1)


print(f'- The media of ages is {average_age:.2f}')

print('- Women registered: ', end='')
women = [p['name'] for p in data1 if p['sex'] == 'F']
print(', '.join(women))

print('- People over 40 (with age):')
for p in data1:
    if p['age'] > 40:
        print(f'{p["name"]} ({p["age"]} years old)')