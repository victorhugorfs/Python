soma = 0
for n in range(6):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é: {}'.format(soma))