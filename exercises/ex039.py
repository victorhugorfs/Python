idade = int(input('Qual a sua idade?: '))
if idade < 18:
    tempo = 18 - idade
    print('Você ainda não precisa se alistar ao Exercito! Falta {} anos para você se alistar!'.format(tempo))
elif idade == 18:
    print('Você precisa se alistar ao Exercito!')
elif idade > 18:
    tempo = idade - 18
    print('Você passou do tempo do alistamento do Exercito! Passou {} anos desde o alistamento!'.format(tempo))