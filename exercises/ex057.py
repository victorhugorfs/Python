sexo = input('Digite o sexo (M/F): ').strip() .upper()
while sexo not in ['M', 'F']:
    print('Valor inválido, por favor, digite M ou F!')
    sexo = input('Digite o sexo (M/F): ').strip() .upper()
print('Sexo {} registrado com sucesso.'.format(sexo))