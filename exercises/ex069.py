print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)

contador = 0       
contadorh = 0      
contadorm = 0      

while True:
    idade = int(input('Idade: '))
    
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    
    if idade >= 18:
        contador += 1
    if sexo == 'M':
        contadorh += 1
    if sexo == 'F' and idade < 20:
        contadorm += 1

    print('-' * 20)
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    print('-' * 20)
    
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {contador}')
print(f'Ao todo temos {contadorh} homem cadastrados')
print(f'E temos {contadorm} mulheres com menos de 20 anos')
