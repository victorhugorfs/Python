from datetime import date
ano_nascimento = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infatil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 20:
    print('Categoria: Sênior')
elif idade > 20:
    print('Categoria: Master')