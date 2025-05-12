valor_casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos você vai pagar a casa?: '))
prestacao = valor_casa / (anos * 12)
if prestacao <= salario * 0.30:
    print('Parabéns o seu empréstimo foi APROVADO!')
else:
    print('Infelizmente não conseguimos aprovar o seu emprestimo!')
print('Para pagar uma casa de R${:.3f} com um salário de R${:.3f} e pagando em {} anos, a prestação será de R${:.3f}!'.format(valor_casa, salario, anos, prestacao))