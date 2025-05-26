contador = 0
soma = 0
numero = int(input('Digite um número inteiro, caso queira que o programe pare digite 999: '))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número inteiro, caso queira que o programe pare digite 999: '))
print('Programa finalizado!')
print('O total de números digitados foi {} e a soma de todos eles foi {}'.format(contador, soma))