frase = str(input('Digite uma frase: ')).strip() .lower() .replace(' ', '')
frase_invertida = frase [::-1]
if frase == frase_invertida:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')