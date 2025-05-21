numero = int(input('Digite um número: '))
original = numero
fatorial = 1
while numero != 0:
    fatorial = fatorial * numero
    numero = numero - 1
print('O fatorial do {} é {}'.format(original, fatorial))