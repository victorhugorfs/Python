nome = input('Digite seu nome completo: ')
nome.strip
nome.upper()
nome.lower()
len(nome.replace(' ',''))
nome.split()[0]
print('Nome completo em maiusculas: {}'.format(nome.upper()))
print('Nome completo em minusculas: {}'.format(nome.lower()))
print('Quantas letras ao todo sem contar os espaços: {}'.format(len(nome.replace(' ',''))))
print('Quantidade de letras no primeiro nome: {}'.format(len(nome.split()[0])))