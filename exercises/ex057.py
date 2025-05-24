sexo = input('Digite o sexo (M/F): ').strip() .upper()[0]
while sexo not in ['M', 'F']:
    print('Valor inválido, por favor, digite M ou F!')
    sexo = input('Digite o sexo (M/F): ').strip() .upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))