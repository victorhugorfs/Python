print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

soma = 0
maior = 0
menor_preco = 0
produto_mais_barato = ''
primeiro = True

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))

    soma += preço

    if preço > 1000:
        maior += 1

    if primeiro or preço < menor_preco:
        menor_preco = preço
        produto_mais_barato = produto
        primeiro = False

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print('-'*40)   
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${menor_preco:.2f}')
