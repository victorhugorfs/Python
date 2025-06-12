import random

numbers = tuple(random.randint(1, 100) for _ in range(5))

max = max(numbers)
min = min(numbers)

print(f'The drawn numbers are: {numbers}')
print(f'The max number drawn is : {max}')
print(f'The min number drawn is: {min}')