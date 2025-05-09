preco = float(input('Valor do produto: '))
pagamento = input('Qual a opção de pagamento? PIX | CARTÃO | 2x CARTÃO | 3x CARTÃO: ').strip().upper()
pix = preco - (preco * 0.10)           
cartao = preco - (preco * 0.05)        
duasvezes_cartao = preco               
tresvezes_cartao = preco + (preco * 0.20)
if pagamento == 'PIX':
    print('O valor do produto pago por Pix fica R${:.2f} já com 10% de desconto!'.format(pix))
elif pagamento == 'CARTÃO':
    print('O valor do produto pago por cartão à vista fica R${:.2f} já com 5% de desconto!'.format(cartao))
elif pagamento == '2X CARTÃO':
    print('O valor do produto pago por cartão parcelado em 2x fica R${:.2f}, sem desconto.'.format(duasvezes_cartao))
elif pagamento == '3X CARTÃO':
    print('O valor do produto pago por cartão parcelado em 3x fica R${:.2f}, com 20% de juros.'.format(tresvezes_cartao))
else:
    print('Opção de pagamento inválida!')