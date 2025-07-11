import random
import time

numbers = list()

def prizedraw():
    for _ in range(5):
        number = random.randint(0, 10)
        numbers.append(number)

    print('Sorted 5 numbers of list:', end=' ')
    for n in numbers:
        print(f'{n}', end=' ')
        time.sleep(0.5)
    print('READY!')

def evensum():
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    print(f'Sum of all even values in {numbers} is {total}')

prizedraw()
evensum()