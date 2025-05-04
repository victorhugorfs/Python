d = float(input('Qual a distância da sua viagem em km?:'))
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('O preço da passagem será R${:.2f}'.format (preco))