n = float(input('Preço do produto:'))
novo = n - (n * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n, novo))