import ex107

price = float(input('Type one price: $'))
print('-'*30)
print(f'Half of {price} is {ex107.half(price)}')
print(f'Twice {price} is {ex107.twice(price)}')
print(f'Increasing 10%, we have {ex107.increasing(price, 10)}')
print(f'Reducing 13%, we have {ex107.reducing(price, 13)}')