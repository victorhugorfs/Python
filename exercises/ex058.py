import random
numero_computador = random.randint(0, 10)
palpite = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 10):'))
erros = 0
while palpite != numero_computador:
    erros += 1
    print('Você errou!')
    palpite = int(input('Tente novamente! Tente adivinhar o número que o computador pensou (entre 0 e 10): '))
print('Você acertou, o número que o computador escolheu foi {}!'.format(palpite))
print('Você tentou adivinhar {} vezes até acertar o número!'.format(erros))