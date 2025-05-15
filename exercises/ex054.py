from datetime import date
import time

print('Digite o ano de nascimento de 7 pessoas!')
time.sleep(1.5)

maiores = 0
menores = 0
ano_atual = date.today().year

for i in range(1, 8):
    ano = int(input(('Ano de nascimento:')))
    idade = ano_atual - ano
    print('Pessoa {}: {} anos'.format(i, idade))
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('Total maiores de idade: {}'.format(maiores))
print('Total menores de idade: {}'.format(menores))