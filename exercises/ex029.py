v = float(input('Qual a velocidade do carro?'))
exesso = v - 80
multa = exesso * 7.00
if v > 80:
    print('Você foi multado no valor de R${:.2f} por estar acima do limite de velocidade que é 80km/h!'.format(multa))
else:
    print('Você está dentro do limite permitido!')
    