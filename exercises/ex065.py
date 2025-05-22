soma = 0
contador = 0
maior = None
menor = None

while True:
    numero = int(input('Digite um número inteiro: '))
    
    soma += numero
    contador += 1
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta != 'S':
        break

media = soma / contador if contador > 0 else 0

print(f'Média dos números digitados: {media}')
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
