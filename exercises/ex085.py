numbers = [[], []]

print('You gonna type 7 values!')

for n in range(7):
    ask = int(input(f'Type value #{n+1}: '))
    if ask % 2 == 0:
         numbers[0].append(ask)
    else:
         numbers[1].append(ask)

print('-='*30)
print(f'The even values typed were: {numbers[0]}')
print(f'The odd values typed were: {numbers[1]}')