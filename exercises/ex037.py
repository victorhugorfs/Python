n = int(input('Digite um número qualquer:'))
r = int(input('Escolha qual será a base de conversão, para BINÁRIO digite 1, para OCTAL digite 2, para HEXADECIMAL digite 3!:'))
if r == 1:
    print('O número digitado convertido para binário é: {}!'.format(bin(n)[2:]))
elif r == 2:
    print('O número digitado convertido para octal é: {}!'.format(oct(n)[2:]))
elif r == 3:
    print('O número digitado convertido para hexadecimal é: {}!'.format(hex(n)[2:]))
else:
    print('Opção inválida!')