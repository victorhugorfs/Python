def readInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except:
            print('ERROR: Please type a valid integer.')

def readFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except:
            print('ERROR: Please type a valid real number.')

num_int = readInt('Enter an integer number: ')
num_float = readFloat('Enter a real number: ')
print(f'The integer value you typed was {num_int} and the real was {num_float}')