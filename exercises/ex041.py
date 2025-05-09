from datetime import date
ano_nascimento = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infatil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')