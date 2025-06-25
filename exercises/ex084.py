people = []

while True:
    name = input('What is your name? ')
    weight = float(input('What is your weight? '))
    people.append([name, weight])

    yorn = input('Do you want to continue? [Y/N] ').strip().upper()[0]
    if yorn == 'N':
        break

print('-=' * 30)
print(f'We have {len(people)} people registered!')

print('\nPeople with weight greater or equal to 100kg:')
has_heavy = False
for p in people:
    if p[1] >= 100:
        print(f'- {p[0]} weighs {p[1]}kg')
        has_heavy = True
if not has_heavy:
    print('We have no record of people over 100kg')

print('\nPeople with weight below 100kg:')
has_light = False
for p in people:
    if p[1] < 100:
        print(f'- {p[0]} weighs {p[1]}kg')
        has_light = True
if not has_light:
    print('We have no record of people under 100kg')
