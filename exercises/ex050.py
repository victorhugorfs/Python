soma = 0
cont = 0
for n in range(6):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você me informou {} números PARES e a soma dos números pares é: {}'.format(cont, soma))