import time

print('Digite o peso de cinco pessoas:')
time.sleep(1.5)

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}ᵃ pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso< menor:
            menor = peso

print('O maior peso foi: {}Kg'.format(maior))
print('O menor peso foi: {}Kg'.format(menor))