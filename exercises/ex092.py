from datetime import date

data0 = dict()
data1 = list()

current_year = date.today().year

for c in range(1):
    data0['name'] = str(input('Name: '))

    birth = int(input('Year of birth: '))
    data0['age'] = current_year - birth

    data0['ctps'] = int(input('Work card (0 does not have one): '))
    if data0['ctps'] == 0:
        print('-=-'*30)
        print(data0)
        print(f'The name is {data0["name"]}')
        print(f'The age is {data0["age"]}')
        print(f'CTPS has value {data0["ctps"]}')
        break
    data0['hiring'] = int(input('Year of hiring: '))
    data0['salary'] = float(input('Salary: '))

    retirement_age = (data0['hiring'] + 35) - birth
    data0['retirement_age'] = retirement_age

    data1.append(data0.copy())

    print('-=-'*30)
    print(data0)
    print(f'The name is {data0["name"]}')
    print(f'The age is {data0["age"]}')
    print(f'CTPS has value {data0["ctps"]}')
    print(f'Hiring was in {data0["hiring"]}')
    print(f'Salary has value {data0["salary"]}')
    print(f'Retirement has value {data0["retirement_age"]}')