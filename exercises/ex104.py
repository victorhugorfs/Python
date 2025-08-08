def read_int(msg):
    while True:
        answer = input(msg)
        if answer.isdigit():
            n = int(answer)
            return n
        else:
            print('ERROR! Enter a valid integer.')
            
n = read_int('Type one number: ')
print(f'You just typed the number: {n}')