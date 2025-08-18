def half(price, format=False):
    result = price / 2

    if format:
        return coin(result)
    else:
        return result

def twice(price, format=False):
    result = price * 2

    if format:
        return coin(result)
    else:
        return result

def increasing(price, percentage, format=False):
    result = price + (price * percentage / 100)   

    if format:
        return coin(result)
    else:
        return result

def reducing(price, percentage, format=False):
    result = price - (price * percentage / 100)

    if format:
        return coin(result)
    else:
        return result

def coin(value):
    return f"${value:.2f}".replace(".", ",")

def summary(price, increase_percent, reduce_percent):
    print('-'*30)
    print('VALUE SUMMARY'.center(30))
    print('-'*30)

    print(f'Analysing price: {coin(price)}')
    print(f'Double the price: {twice(price, True)}')
    print(f'Half price: {half(price, True)}')
    print(f'{increase_percent}% increase: {increasing(price, increase_percent, True)}')
    print(f'{reduce_percent}% of reduction: {reducing(price, reduce_percent, True)}')

    print('-'*30)