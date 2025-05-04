v = int(input('Qual a velocidade do carro?'))
exesso = v - 80
multa = exesso * 7.00
if v > 80:
    print('Você foi multado no valor de R${:.2f} por estar acima do limite de velocidade!'.format(multa))
else:
    print('Você está dentro do limite permitido!')