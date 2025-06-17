values = []

for i in range(5):
    value = int(input(f'Type one value for position {i}: '))
    values.append(value)
print('-=-'*20)
print(f'You type this values {values}')
print(f'The biggest value type was {max(values)} in positions {[i for i, v in enumerate(values) if v == max(values)]}')
print(f'The small value type was {min(values)} in positions {[i for i, v in enumerate(values) if v == min(values)]}')