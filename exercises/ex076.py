product_price = ('Keyboard', 300, 'Pc Gamer', 7000, 'Mouse', 400, 'MousePad', 90, 'Monitor', 1000)

print('-'*30)
print('PRICE LIST'.center(30))
print('-'*30)
for pos in range (0, len(product_price)):
    if pos % 2 == 0:
        print(f'{product_price[pos]:.<30}', end='')
    else:
        print(f'${product_price[pos]:>7.2f}')
print('-'*30)