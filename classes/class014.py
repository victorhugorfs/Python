#n = 1
#while n != 0:
#    n = int(input('Digite um valor: '))
#print('Fim!')

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N]' )).upper()
#print('Fim')

n = 1
par = impar = 0 #pode fazer um em cada linha também!
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))