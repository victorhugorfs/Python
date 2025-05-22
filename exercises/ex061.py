primeiro = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
print('Os 10 primeiros termos da PA são:')
contador = 0
while contador < 10:
    print(primeiro)
    contador += 1
    primeiro += razao