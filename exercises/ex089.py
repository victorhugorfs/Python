data = []

while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))

    student = [name, [grade1, grade2], (grade1 + grade2) / 2]
    data.append(student)

    cont = str(input('Do you wanna continue? [S/N]')).strip().upper()[0]

    if cont == 'N':
        break

print('-=-'*30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-=-'*30)

for index, student in enumerate(data):
    print(f'{index:<4}{student[0]:<10}{student[2]:>8.1f}')

while True:
    print('-'*40)
    option = int(input('Show grades for which student? (999 to stop): '))
    if option == 999:
        break
    if 0 <= option < len(data):
        print(f'Grades for {data[option][0]} are {data[option][1]}')