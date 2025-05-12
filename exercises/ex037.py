n = int(input('Digite um número qualquer:'))
r = int(input('Escolha qual será a base de conversão: [1] converter para BINÁRIO [2] converter para OCTAL [3] converter para HEXADECIMAL - Sua opção:'))
if r == 1:
    print('O número digitado convertido para binário é: {}!'.format(bin(n)[2:]))
elif r == 2:
    print('O número digitado convertido para octal é: {}!'.format(oct(n)[2:]))
elif r == 3:
    print('O número digitado convertido para hexadecimal é: {}!'.format(hex(n)[2:]))
else:
    print('Opção inválida!')