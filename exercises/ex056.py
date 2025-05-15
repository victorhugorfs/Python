soma_idades = 0
mais_velho_nome = ''
mais_velho_idade = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo, [H] = Homem - [M] = Mulher: '))
    
    soma_idades += idade  
    
    if sexo.upper() == 'H':  
        if idade > mais_velho_idade:
            mais_velho_idade = idade
            mais_velho_nome = nome
            
    if sexo.upper() == 'M' and idade < 20:  
        mulheres_menos_20 += 1

media_idade = soma_idades / 4
print('A média de idade do grupo é {:.1f} anos.'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos.'.format(mais_velho_nome, mais_velho_idade))
print('{} mulher(es) têm menos de 20 anos.'.format(mulheres_menos_20))
