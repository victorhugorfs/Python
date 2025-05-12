preco = float(input('Valor do produto: '))
pagamento = int(input('Qual a opção de pagamento? [1] PIX | [2] CARTÃO | [3] 2x CARTÃO | [4] 3x CARTÃO - Qual é a opção: '))
pagamento1 = preco - (preco * 0.10)   #pix       
pagamento2 = preco - (preco * 0.05)   #cartao        
pagamento3 = preco                    #2x cartao               
pagamento4 = preco + (preco * 0.20)   #3x cartao
if pagamento == 1:
    print('O valor do produto pago por Pix fica R${:.2f} já com 10% de desconto!'.format(pagamento1))
elif pagamento == 2:
    print('O valor do produto pago por cartão à vista fica R${:.2f} já com 5% de desconto!'.format(pagamento2))
elif pagamento == 3:
    print('O valor do produto pago por cartão parcelado em 2x fica R${:.2f}, sem desconto.'.format(pagamento3))
elif pagamento == 4:
    print('O valor do produto pago por cartão parcelado em 3x fica R${:.2f}, com 20% de juros.'.format(pagamento4))
else:
    print('Opção de pagamento inválida!')