import random
numero_computador = random.randint(0, 5)
palpite = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 5):'))
if palpite == numero_computador:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número era {}'.format(numero_computador))